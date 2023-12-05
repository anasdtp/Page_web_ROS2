from flask import Flask
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from threading import Thread


app = Flask(__name__)
ros_message = "Aucun message reçu"


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        global ros_message
        ros_message = msg.data


def run_ros_node():
    rclpy.init()
    ros_node = MinimalSubscriber()
    rclpy.spin(ros_node)
    rclpy.shutdown()


def run_flask():
    app.run(host='192.168.188.129', port=8080, debug=True)


@app.route('/')
def home():
    return f'Hello, World! ROS Message: {ros_message}'

def main():
    # run_ros_node()
    ros_thread = Thread(target=run_ros_node)
    ros_thread.start()

    run_flask()

    

if __name__ == '__main__':
    main()
