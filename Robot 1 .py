
# My first robot

for distance in [20, 15, 8, 3, 12]:
    print(f"I see an obstacle distance m : ", end="")
    if distance < 10:
        print("Turning right!")
    else:
        print("moving fast!")
import time
import random

class ObstacleAvoidingRobot:
    def __init__(self):
        self.battery = 100
        self.distance_traveled = 0
        self.obstacles_avoided = 0

    # SENSORS
    def get_front_distance(self):
        return random.randint(5, 150)

    def get_left_distance(self):
        return random.randint(10, 120)

    def get_right_distance(self):
        return random.randint(10, 120)

    # SMOOTH CURVED MOTORS - CURVE, NOT SHARP
    def forward_smooth(self, speed):
        print(f"  -> Moving forward smooth at {speed}% - curved path")
        self.distance_traveled += 1

    def curve_left_smooth(self, speed):
        print(f"  -> Curving left smoothly at {speed}% - long curve")
        self.distance_traveled += 1

    def curve_right_smooth(self, speed):
        print(f"  -> Curving right smoothly at {speed}% - long curve")
        self.distance_traveled += 1

    def backward_smooth(self, speed):
        print(f"  -> Moving backward smooth at {speed}%")

    def stop_smooth(self):
        print(f"  -> Smooth stop - decelerating in curve")

    # CURVED DECISION LOGIC - LONG AND CURVED
    def run_curved_mission(self):
        print("="*60)
        print("OBSTACLE AVOIDING ROBOT - CURVED LONG PATH")
        print("="*60)
        print(f"Battery: {self.battery}%")
        print("Mode: Smooth Curved Avoidance - Long Mission")
        print("="*60)

        for step in range(1, 61):
            if self.battery <= 5:
                print("Battery too low, ending curved mission")
                break

            front = self.get_front_distance()
            left = self.get_left_distance()
            right = self.get_right_distance()

            print(f"\n[STEP {step}/60] Front: {front}cm | Left: {left}cm | Right: {right}cm")

            # LONG CURVED LOGIC
            if front > 90:
                self.forward_smooth(85)
                print("  -> Path clear, long forward curve")

            elif front > 70:
                self.forward_smooth(65)
                print("  -> Long distance, slight curve forward")

            elif front > 50:
                if left > right:
                    self.curve_left_smooth(50)
                    print("  -> Curving left, long smooth arc")
                else:
                    self.curve_right_smooth(50)
                    print("  -> Curving right, long smooth arc")
                self.obstacles_avoided += 1

            elif front > 30:
                self.stop_smooth()
                time.sleep(0.2)
                if left > 60:
                    self.curve_left_smooth(40)
                    self.curve_left_smooth(40)
                    print("  -> Double left curve to avoid - long curve")
                elif right > 60:
                    self.curve_right_smooth(40)
                    self.curve_right_smooth(40)
                    print("  -> Double right curve to avoid - long curve")
                else:
                    self.backward_smooth(30)
                    self.curve_left_smooth(60)
                    print("  -> Backward then long curve")
                self.obstacles_avoided += 1

            else:
                print("  -> Very close! Emergency curved escape")
                self.stop_smooth()
                self.backward_smooth(60)
                time.sleep(0.5)
                self.curve_right_smooth(70)
                self.curve_right_smooth(70)
                self.obstacles_avoided += 1

            self.battery -= 1
            print(f"  -> Battery: {self.battery}% | Traveled: {self.distance_traveled}m | Avoided: {self.obstacles_avoided}")

            time.sleep(0.35)

        print("\n" + "="*60)
        print("CURVED LONG MISSION COMPLETE")
        print("="*60)
        print(f"Total steps: 60")
        print(f"Distance: {self.distance_traveled} meters - LONG")
        print(f"Curved avoids: {self.obstacles_avoided}")
        print(f"Battery left: {self.battery}%")
        print("Path type: Always curved, always long")
        print("="*60)

# START THE LONG CURVED ROBOT
robot = ObstacleAvoidingRobot()
robot.run_curved_mission()