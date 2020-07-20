import os
from dataclasses import dataclass
import glob
import shutil
import logging
import pele_platform.Utilities.Helpers.solventOBCParamsGenerator as obc
import pele_platform.Utilities.Parameters.pele_env as pv
import pele_platform.constants.constants as cs

@dataclass
class ImplicitSolvent:
    
    solvent: str
    obc_tmp: str
    template_folder: str
    obc_file: str
    logger: logging.Logger
    forcefield: str=""

    def generate(self):
        self.enforce_obc_with_openff()
        self.logger.info("Setting implicit solvent: {}".format(self.solvent))
        self.set_implicit_solvent()
        self.logger.info("Implicit solvent set\n\n".format(self.solvent))

    def enforce_obc_with_openff(self):
        if self.forcefield == cs.OPENFORCEFIELD:
            self.solvent = "OBC"

    def set_implicit_solvent(self):
        if self.solvent == "OBC": #OBC from ...
            shutil.copy(self.obc_tmp, self.obc_file)
            for template in glob.glob(os.path.join(self.template_folder, "*")):
                obc.main(template, self.obc_file)
        else:
            pass #SVG by default
