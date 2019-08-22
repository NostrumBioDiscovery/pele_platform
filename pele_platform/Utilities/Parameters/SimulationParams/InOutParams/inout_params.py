import pele_platform.constants as cs

class InOutParams(object):


    def __init__(self, args):
        self.exit_value = args.exit_value if args.exit_value else self.simulation_params["exit_value"]
        self.exit_condition = args.exit_condition
        self.exit_trajnum = args.exit_trajnum
        self.bias_column = args.bias_column if args.bias_column else self.simulation_params["bias_column"]
        #If User inputs exit condition or when doing an exit simulation
        if args.exit or args.in_out or args.in_out_soft:
            self.unbinding_block = cs.UNBINDING.format(self.bias_column, self.exit_value, self.exit_condition, self.exit_trajnum)
            self.equilibration = "true"
        else:
            self.unbinding_block = ""
