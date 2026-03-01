class Solution:
    def sampleStats(self, count):
        total_count = 0
        total_sum = 0
        
        minimum = -1
        maximum = -1
        mode = 0
        highest_frequency = 0

        for i in range(256):
            if count[i] > 0:
                if minimum == -1:
                    minimum = i

                maximum = i
                total_count += count[i]
                total_sum += i * count[i]

                if count[i] > highest_frequency:
                    highest_frequency = count[i]
                    mode = i

        mean = total_sum / total_count

        cumulative_count = 0
        middle1 = None
        middle2 = None

        if total_count % 2 == 1:
            middle_position = total_count // 2 + 1
            
            for i in range(256):
                cumulative_count += count[i]
                if cumulative_count >= middle_position:
                    median = i
                    break
        else:
            middle_position1 = total_count // 2
            middle_position2 = middle_position1 + 1
            
            for i in range(256):
                cumulative_count += count[i]
                
                if cumulative_count >= middle_position1 and middle1 is None:
                    middle1 = i
                
                if cumulative_count >= middle_position2:
                    middle2 = i
                    break
            
            median = (middle1 + middle2) / 2

        return [float(minimum), float(maximum), float(mean), float(median), float(mode)]