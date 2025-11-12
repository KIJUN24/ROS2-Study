# ROS2를 사용하기 위한 노드 import
import rclpy
from rclpy.node import Node

# 데이터를 주고 받을 형식(String) import
from std_msgs.msg import String

# 클래스 만들기
class PublisherStudy(Node):
    # 초기 함수 선언
    def __init__(self):
        # 노드의 이름은 'publisher_studying'로 선언
        super().__init__('publisher_studying')
        # 데이터를 줄 변수 선언(Pub)
        # String 타입을 'topic'이라는 이름으로 보내겠다. Queue 사이즈는 10
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        # self.time_callback을 위한 변수 -> 0.5초
        timer_period = 0.5  # seconds
        # time_callback을 0.5초마다 한 번씩 실행시키겠다.
        self.timer = self.create_timer(time_period, self.timer_callback)
        # 1씩 증가시킬 변수 선언
        self.i = 0

    # 동작: time_callback 함수 선언
    def time_callback(self):
        # messgae의 타입은 String이다.
        msg = String()
        # message에 담을 data는 'Hello World: %d'.
        # %d에는 정수인 i가 들어감.
        msg.data = 'Hello World: %d' % self.i
        # __init__(self)에서 선언한 self.publisher_ 변수가 msg를 pub함.
        self.publisher_.publish(msg)
        # self.get_logger().info == print()
        # self.get_logger().info 이걸 사용해야 상대적으로 delay가 안 생긴다.
        self.get_logger().info('Publishing: "%s"' % msg.data)
        # 코드가 한 번 돌아갈 때마다 i값 1증가.
        self.i += 1

# 실제 코드가 돌아가는 main 함수
def main(args=None):
    # ros2를 사용하기 위함.
    # ROS2 시스템 초기화.
    rclpy.init(args=args)
    # 변수에 PublisherStudy() 클래스 대입
    publisher_study = PublisherStudy()
    # publisher_study 계속 구동시켜라.
    rclpy.spin(publisher_study)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
    # ROS2 관련 리소스들 Clean up
    # 안전하게 종료하기 위함.
    publisher_study.destroy_node()
    # ROS2 전체 종료
    rclpy.shutdown()

# 이 파일이 직접 실행될 때만 main() 함수를 실행시켜라.
if __name__ == '__main__':
    main()
