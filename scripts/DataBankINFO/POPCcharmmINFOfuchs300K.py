DOI="10.5281/zenodo.1306800"
user_information = """
POPC CHARMM fuchs 300K
#NMRLIPIDS BEGIN

@SIM
@SYSTEM=POPC_T300K
@MAPPING=POPC,mappingPOPCcharmm.txt
@SOFTWARE=gromacs
@FF=CHARMM36
@FF_SOURCE=??
@FF_DATE=??
@TRJ=md_dt100_OK_centered.xtc
@TPR=md.tpr
@PREEQTIME=0
@TIMELEFTOUT=50

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
dir_wrk = "/media/osollila/Data/tmp/DATABANK/"
