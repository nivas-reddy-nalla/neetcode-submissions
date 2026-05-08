class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for p, s in cars:
            # Use float division for accuracy
            arrival_time = (target - p) / s
            
            # If the stack is empty or the current car takes LONGER 
            # than the fleet in front, it starts a new fleet.
            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
            
            # If arrival_time <= stack[-1], the car joins the existing fleet
            # (we do nothing, effectively letting it "merge" into the slower car)
                    
        return len(stack)