
### Create a bash file for downloading from GEO in the terminal, saved in parent folder of "GSE" data folder:
   ```console
   nano geofetch_download.sbatch
   ```
   Paste your script below
   ```console
#!/bin/bash
#SBATCH --job-name=geofetch_download
#SBATCH --output=geofetch_%j.out
#SBATCH --error=geofetch_%j.err
#SBATCH --time=12:00:00
#SBATCH --mem=32G
#SBATCH --cpus-per-task=4
#SBATCH --account=PAS2556

### This file is used to directly download the file from GEO dataset

module load anaconda
conda activate base   # the environment install geofetch

# ==== Check parameter ====
if [ -z "$1" ]; then
    echo "Usage: sbatch geofetch_download.sbatch <GSE_ID>"
    exit 1
fi

GSE=$1

# ==== Output path ====
BASEDIR=/fs/ess/PAS2556/Bioinformatics_analysis/Human.DRG.Omics.Data/datasets/RNA.data/Download.data/$GSE
METADIR=$BASEDIR/metadata
DATADIR=$BASEDIR/download

mkdir -p $METADIR $DATADIR

# ==== Download ====
echo "[INFO] Starting geofetch for $GSE ..."
geofetch -i $GSE --processed --geo-folder $DATADIR -m $METADIR
echo "[INFO] Finished $GSE"
   ```


### Submit the bash file (add the number of GEO at the end of the command):
   ```console
   sbatch geofetch_download.sbatch GSE169301
   squeue -u osc_username
   ```
