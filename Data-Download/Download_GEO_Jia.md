#!/bin/bash
#SBATCH --job-name=geofetch_download
#SBATCH --output=geofetch_%j.out
#SBATCH --error=geofetch_%j.err
#SBATCH --time=12:00:00
#SBATCH --mem=32G
#SBATCH --cpus-per-task=4
#SBATCH --account=PAS2556

module load anaconda
conda activate base   # 你安装 geofetch 的环境

# ==== 参数检查 ====
if [ -z "$1" ]; then
    echo "Usage: sbatch geofetch_download.sbatch <GSE_ID>"
    exit 1
fi

GSE=$1

# ==== 输出目录 ====
BASEDIR=/fs/ess/PAS2556/Bioinformatics_analysis/Human.DRG.Omics.Data/datasets/RNA.data/Download.data/$GSE
METADIR=$BASEDIR/metadata
DATADIR=$BASEDIR/download

mkdir -p $METADIR $DATADIR

# ==== 下载 ====
echo "[INFO] Starting geofetch for $GSE ..."
geofetch -i $GSE --processed --geo-folder $DATADIR -m $METADIR
echo "[INFO] Finished $GSE"
