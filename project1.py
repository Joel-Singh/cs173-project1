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
        remainder = time % (p_in + p_out)
        return remainder < p_in

    return is_currently_in(t_hop, p1_in, p1_out) or is_currently_in(t_hop, p2_in, p2_out)
    

p1_in = 5
p1_out = 1

p2_in = 5 
p2_out = 1

t_hop = 5

def main():
    if soprano_is_caught(p1_in, p1_out, p2_in, p2_out, t_hop):
        print("CAUGHT")
    else:
        print("SUCCESS")

if __name__ == "__main__":
    main()
