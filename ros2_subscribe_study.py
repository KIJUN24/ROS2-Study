# ROS2를 사용하기 위한 노드 import
import rclpy
from rclpy.node import Node

# 데이터를 주고 받을 형식(String) import
from std_msgs.msg import String

# 클래스 만들기
class SubscriberStudy(Node):
    # 초기 함수 선언
    def __init__(self):
        # 노드의 이름은 'subscriber_studying'로 선언
        super().__init__('subscriber_studying')
        # 데이터를 받을 변수 선언(Pub)
        # String 타입을 'topic'이라는 이름으로 self.listen_callback()로 받겠다. Queue 사이즈는 10
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listene_callback,
            10)
        # 사용하지 않는 변수 경고 방지
        self.subscription  # prevent unused variable warning

    # 동작: listene_callback 함수 선언
    def listene_callback(self, msg):
        # self.get_logger().info == print()
        # message를 받은 data를 터미널에서 확인.
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    # ROS2 시스템 초기화
    rclpy.init(args=args)
    # 클래스를 사용하기 위한 변수.
    subscriber_study = SubscriberStudy()
    # 노드 실행 (대기 상태 유지)
    # publisher_study 계속 구동시켜라.
    rclpy.spin(subscriber_study)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
    # ROS2 관련 리소스들 Clean up
    # 안전하게 종료하기 위함.
    subscriber_study.destroy_node()
    # ROS2 전체 종료
    rclpy.shutdown()


if __name__ == '__main__':
    main()
