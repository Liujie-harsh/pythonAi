from matplotlib import transforms
from matplotlib.colors import Normalize
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
import torch
import numpy as np
from sklearn.metrics import accuracy_score
from tqdm import tqdm
from torch import nn


def load_fashion_mnist(batch_size=64, shuffle=True):
    """
    Load Fashion MNIST dataset
    Args:
        batch_size: batch size for dataloader
        shuffle: whether to shuffle the data
    Returns:
        train_dataloader: DataLoader for training data
        test_dataloader: DataLoader for test data
    """
    # Download training data
    training_data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=True,
        transform=ToTensor()
    )

    # Download test data 
    test_data = datasets.FashionMNIST(
        root="data",
        train=False,
        download=True,
        transform=ToTensor()
    )

    # Create data loaders
    train_dataloader = torch.utils.data.DataLoader(training_data, batch_size=batch_size, shuffle=True)
    test_dataloader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=False)

    return train_dataloader, test_dataloader


class EarlyStopCallback:
    def __init__(self, patience=5, min_delta=0.01):
        """
        Early stopping implementation to prevent overfitting
        Args:
            patience (int, optional): Number of epochs with no improvement after which training will be stopped. Defaults to 5.
            min_delta (float, optional): Minimum change in the monitored quantity to qualify as an improvement, i.e. an absolute 
                change of less than min_delta, will count as no improvement. Defaults to 0.01.
        """
        self.patience = patience
        self.min_delta = min_delta
        self.best_metric = -1
        self.counter = 0
        
    def __call__(self, metric):
        if metric >= self.best_metric + self.min_delta:
            # update best metric
            self.best_metric = metric
            # reset counter 
            self.counter = 0
        else: 
            self.counter += 1
            
    @property
    def early_stop(self):
        return self.counter >= self.patience


@torch.no_grad()
def evaluating(model, dataloader, loss_fct, device):
    """
    Evaluate the model on the validation dataset
    Args:
        model: PyTorch model to evaluate
        dataloader: DataLoader with validation data
        loss_fct: Loss function
        device: Device to run the model on
    Returns:
        mean_loss: Mean loss on the validation set
        acc: Accuracy on the validation set
    """
    loss_list = []
    pred_list = []
    label_list = []
    for datas, labels in dataloader:
        datas = datas.to(device)
        labels = labels.to(device)
        # Forward pass
        logits = model(datas)
        loss = loss_fct(logits, labels)         # Validation loss
        loss_list.append(loss.item())
        
        preds = logits.argmax(axis=-1)    # Validation predictions, argmax takes the index of the maximum value
        pred_list.extend(preds.cpu().numpy().tolist()) # Convert predictions to list
        label_list.extend(labels.cpu().numpy().tolist())
        
    acc = accuracy_score(label_list, pred_list)
    return np.mean(loss_list), acc


def training(
    model, 
    train_loader, 
    val_loader, 
    epoch, 
    loss_fct, 
    optimizer, 
    device,
    early_stop_callback=None,
    eval_step=500,
    ):
    """
    Train the model
    Args:
        model: PyTorch model to train
        train_loader: DataLoader with training data
        val_loader: DataLoader with validation data
        epoch: Number of epochs to train for
        loss_fct: Loss function
        optimizer: Optimizer
        device: Device to run the model on
        tensorboard_callback: Callback for TensorBoard logging
        save_ckpt_callback: Callback to save model checkpoints
        early_stop_callback: Callback for early stopping
        eval_step: Steps between evaluations
    Returns:
        record_dict: Dictionary with training and validation metrics
    """
    record_dict = {
        "train": [],
        "val": []
    }
    
    global_step = 0
    model.train()
    with tqdm(total=epoch * len(train_loader)) as pbar:
        for epoch_id in range(epoch):
            # training
            for datas, labels in train_loader:
                datas = datas.to(device)
                labels = labels.to(device)
                # Zero gradients
                optimizer.zero_grad()
                # Forward pass
                logits = model(datas)
                # Compute loss
                loss = loss_fct(logits, labels)
                # Backward pass
                loss.backward()
                # Update weights
                optimizer.step()
                preds = logits.argmax(axis=-1)        
                acc = accuracy_score(labels.cpu().numpy(), preds.cpu().numpy())    
                loss = loss.cpu().item()
                
                # Record metrics
                record_dict["train"].append({
                    "loss": loss, "acc": acc, "step": global_step
                })
                
                # Evaluate
                if global_step % eval_step == 0:
                    model.eval()
                    val_loss, val_acc = evaluating(model, val_loader, loss_fct, device)
                    record_dict["val"].append({
                        "loss": val_loss, "acc": val_acc, "step": global_step
                    })
                    model.train()
                    
                    if early_stop_callback is not None:
                        early_stop_callback(val_acc)
                        if early_stop_callback.early_stop:
                            print(f"Early stop at epoch {epoch_id} / global_step {global_step}")
                            return record_dict
                    
                # Update step
                global_step += 1
                pbar.update(1)
                pbar.set_postfix({"epoch": epoch_id})
        
    return record_dict
