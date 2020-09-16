DOI="10.5281/zenodo.1129415"

user_information = """
POPS
#NMRLIPIDS BEGIN

@SIM
@MAPPING=POPS,mappingPOPScharmm.txt
@SYSTEM=POPS_298K
@SOFTWARE=gromacs
@FF=CHARMM36
@FF_SOURCE=CHARMM-GUI
@FF_DATE=??
@TRJ=md-CHARMM36_10A-switch_POPS_v1_400-500ns_skip10.xtc
@TPR=for-md-CHARMM36_POPS_298K_v1.tpr
@PREEQTIME=400
@TIMELEFTOUT=0


@POPC=POPC
@POPG=POPG
@POPS=POPS
@POPE=POPE

@POT=M_K_M
@SOD=M_NA_M
@CLA=M_CL_M
@CAL=M_CA_M
@SOL=M_SOL_M

@NPOPC=[0,0]
@NPOPG=[0,0]
@NPOPS=[0,0]
@NPOPE=[0,0]

@NPOT=0
@NSOD=0
@NCLA=0
@NCAL=0
@NSOL=0

@TEMPERATURE=0
@TRJLENGTH=0


#NMRLIPIDS END

"""


# Working directory
dir_wrk  = "/media/osollila/Data/tmp/DATABANK/"
