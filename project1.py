# Need to figure out what to do if the sum of p_in and  p_out is greater than 24
def soprano_is_caught(p1_in, p1_out, p2_in, p2_out, t_hop):
    """
    Returns a bool indicating whether soprano is caught

    Args:
      p1_in (integer):  length of time (in minutes) person 1 stays in the kitchen
      p1_out (integer): length of time (in minutes) person 1 stays out of the kitchen
      p2_in (integer): length of time (in minutes) person 2 stays in the kitchen
      p2_out (integer): length of time (in minutes) person 2 stays out of the kitchen
      t_hop (integer): the time in minutes after midnight when Soprano attempts to hop

    Returns:
        bool: Whether soprano is caught
    """
    def is_currently_in(time, p_in, p_out):
        time_as_hours = float(time)/60
        time_as_hours = time_as_hours % 24

        time = float(time_as_hours) * 60

        remainder = time % (p_in + p_out)
        return remainder < p_in

    return is_currently_in(t_hop, p1_in, p1_out) or is_currently_in(t_hop, p2_in, p2_out)
    

def main():
    p1_in = int(input())
    p1_out = int(input())

    p2_in = int(input())
    p2_out = int(input())

    t_hop = int(input())

    if soprano_is_caught(p1_in, p1_out, p2_in, p2_out, t_hop):
        print("CAUGHT")
    else:
        print("SUCCESS")

if __name__ == "__main__":
    main()
