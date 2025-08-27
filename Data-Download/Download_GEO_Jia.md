
### Create a bash file for downloading from GEO in the terminal, return folders: download and metadata under "$GSE" data folder:
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
BASEDIR=/fs/ess/PAS2556/Bioinformatics_analysis/Human.DRG.Omics.Data/datasets/RNA.data/$GSE
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

### Other download command in terminal:
1. Copy the link address of file
   ```console
   wget -P /fs/ess/PAS2556/Bioinformatics_analysis/Human.DRG.Omics.Data/datasets/RNA.data/GSE201586/download "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE201586&format=file"
   ```
2. Unpack the .tar file in python
   ```console
import tarfile

file_path = "GSE201586_RAW.tar"
output_dir = "./GSE201586_RAW"

# open tar file
with tarfile.open(file_path, "r") as tar:
    tar.extractall(path=output_dir)  
    print("Done, saved in", output_dir)
   ```
