# 作者:python11-刘杰
# 2025年06月06日21时51分10秒
# xxx@qq.com

# 导入必要的模块
import pygame  # 游戏开发模块
import sys    # 系统模块，用于退出程序

# 定义颜色常量，使用RGB值表示
WHITE = (255, 255, 255)  # 白色，用于玩家挡板
RED = (255, 0, 0)       # 红色，用于小球
BLACK = (0, 0, 0)       # 黑色，用于背景

class Player:
    """玩家控制的挡板类"""
    def __init__(self):
        # 创建一个矩形对象表示挡板，参数为：x坐标、y坐标、宽度、高度
        self.rect = pygame.Rect(350, 550, 100, 20)

    def move(self, direction):
        """移动挡板
        Args:
            direction (str): 移动方向，"left"表示左移，"right"表示右移
        """
        # 检查边界，确保挡板不会移出屏幕
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= 5  # 向左移动5个像素
        if direction == "right" and self.rect.right < 800:
            self.rect.x += 5  # 向右移动5个像素

    def draw(self, screen):
        """在屏幕上绘制挡板
        Args:
            screen: pygame的屏幕对象
        """
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    """游戏中的球类"""
    def __init__(self):
        # 创建一个矩形对象表示球，参数为：x坐标、y坐标、宽度、高度
        self.rect = pygame.Rect(400, 300, 15, 15)
        # 球的移动速度，[x方向速度, y方向速度]
        self.speed = [3, 3]

    def move(self):
        """更新球的位置"""
        self.rect.x += self.speed[0]  # 更新x坐标
        self.rect.y += self.speed[1]  # 更新y坐标

    def bounce(self, axis):
        """处理球的反弹
        Args:
            axis (int): 0表示x轴反弹，1表示y轴反弹
        """
        self.speed[axis] *= -1  # 反转指定轴的速度方向

    def draw(self, screen):
        """在屏幕上绘制球
        Args:
            screen: pygame的屏幕对象
        """
        pygame.draw.rect(screen, RED, self.rect)

class Game:
    """主游戏类，控制游戏的整体逻辑"""
    def __init__(self):
        """初始化游戏"""
        pygame.init()  # 初始化pygame
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("接球游戏")  # 设置窗口标题
        self.clock = pygame.time.Clock()  # 创建时钟对象，控制游戏帧率
        self.font = pygame.font.Font(None, 36)  # 创建字体对象，用于显示得分
        self.player = Player()  # 创建玩家挡板
        self.ball = Ball()     # 创建球
        self.score = 0         # 初始化得分
        self.running = True    # 游戏运行状态标志

    def reset(self):
        """重置游戏状态"""
        self.score = 0  # 重置得分
        self.player = Player()  # 重置玩家位置
        self.ball = Ball()      # 重置球的位置和速度

    def run(self):
        """游戏主循环"""
        while self.running:
            # 处理游戏事件
            for event in pygame.event.get():
                # 检查是否点击关闭窗口
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # 获取键盘按键状态
            keys = pygame.key.get_pressed()
            # 处理玩家输入
            if keys[pygame.K_LEFT]:
                self.player.move("left")
            if keys[pygame.K_RIGHT]:
                self.player.move("right")

            # 更新球的位置
            self.ball.move()

            # 处理碰撞
            # 检查球是否碰到左右边界
            if self.ball.rect.left <= 0 or self.ball.rect.right >= 800:
                self.ball.bounce(0)  # x轴反弹
            # 检查球是否碰到上边界
            if self.ball.rect.top <= 0:
                self.ball.bounce(1)  # y轴反弹
            # 检查球是否碰到玩家挡板
            if self.ball.rect.colliderect(self.player.rect):
                self.ball.bounce(1)  # y轴反弹
                self.score += 1      # 增加得分

            # 检查游戏是否结束（球触底）
            if self.ball.rect.bottom >= 600:
                print(f"游戏结束！得分: {self.score}")
                self.running = False

            # 绘制游戏画面
            self.screen.fill(BLACK)  # 填充背景色
            self.player.draw(self.screen)  # 绘制玩家挡板
            self.ball.draw(self.screen)    # 绘制球
            # 显示得分
            score_text = self.font.render(f"得分: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            # 更新显示
            pygame.display.flip()
            # 控制游戏帧率为60FPS
            self.clock.tick(60)

# 程序入口
if __name__ == "__main__":
    game = Game()  # 创建游戏实例
    game.run()     # 运行游戏