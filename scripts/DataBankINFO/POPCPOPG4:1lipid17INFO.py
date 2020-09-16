DOI="10.5281/zenodo.3693681"
user_information = """
POPC:POPG (4:1) lipid17
#NMRLIPIDS BEGIN

@SIM
@SYSTEM=POPC:POPG(4:1)_T298K
@MAPPING=POPC,mappingPOPClipid17ecc.txt,POPG,mappingPOPGlipid17ecc.txt
@SOFTWARE=gromacs
@FF=lipid17
@FF_SOURCE=10.5281/zenodo.2585523
@FF_DATE=??
@TRJ=trajSKIP.xtc
@TPR=topol.tpr
@PREEQTIME=50
@TIMELEFTOUT=0

@POPC=PC
@POPG=PGR
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
