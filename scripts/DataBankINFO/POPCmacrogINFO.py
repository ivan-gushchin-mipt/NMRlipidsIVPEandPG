DOI="10.5281/zenodo.3741793"
user_information = """
POPC macrog from Rodiquez and Fuchs
#NMRLIPIDS BEGIN

@SIM
@SYSTEM=POPC:POPE(1:1)_T300K
@MAPPING=POPC,mappingPOPCmacrogFUCHS.txt
@SOFTWARE=gromacs
@FF=MacRog
@FF_SOURCE=10.5281/zenodo.3725637
@FF_DATE=26/3/2020
@TRJ=md_OK_100.xtc
@TPR=md.tpr
@PREEQTIME=0
@TIMELEFTOUT=200

@POPC=POPC
@POPG=POPG
@POPS=POPS
@POPE=POPE

@POT=K
@SOD=NA
@CLA=CL
@CAL=CA
@SOL=SOL

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