import os
import re
import requests
import urllib.request

def download_gse_supplementary_files(gse_id: str,download_dir: str):
    """
    Finds and downloads all supplementary files for a given GEO Series ID (GSE).

    Args:
        gse_id (str): The GEO Series ID (e.g., "GSE280731").
    """
    print(f"--- Starting download for {gse_id} ---")

    # 1. Fetch the metadata record from GEO
    # This URL provides the full metadata in a simple text format.
    metadata_url = f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={gse_id}&targ=self&view=full&form=text"
    
    try:
        print(f"Fetching metadata from: {metadata_url}")
        response = requests.get(metadata_url)
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching metadata for {gse_id}: {e}")
        return

    # 2. Find all supplementary file FTP links in the metadata
    ftp_links = []
    # The metadata contains lines like: !Series_supplementary_file = ftp://...
    # We use a regular expression to find all such lines and extract the URL.
    pattern = r"!Series_supplementary_file = (ftp://.+)"
    
    for line in response.text.splitlines():
        match = re.match(pattern, line)
        if match:
            ftp_links.append(match.group(1).strip())

    if not ftp_links:
        print(f"No supplementary files found for {gse_id}.")
        print("This could be because the series has no supplementary files or they are part of the main RAW.tar file.")
        return

    print(f"Found {len(ftp_links)} supplementary file(s).")

    # 3. Create a directory to store the files
    output_dir = download_dir
    os.makedirs(output_dir, exist_ok=True)
    print(f"Files will be saved in: '{os.path.abspath(output_dir)}'")

    # 4. Download each file
    for i, link in enumerate(ftp_links):
        # Extract the filename from the FTP link
        filename = link.split('/')[-1]
        output_path = os.path.join(output_dir, filename)
        
        print(f"\nDownloading file {i+1} of {len(ftp_links)}:")
        print(f"  Source: {link}")
        print(f"  Destination: {output_path}")

        try:
            # Use urlretrieve to download the file from the FTP link
            urllib.request.urlretrieve(link, output_path)
            print(f"  Success: '{filename}' downloaded.")
        except Exception as e:
            print(f"  Error: Failed to download {filename}. Reason: {e}")

    print(f"\n--- Download process for {gse_id} complete. ---")

if name == "main":
    # --- USAGE EXAMPLE ---
    # Replace this with the GSE ID you want to download
    target_gse_id = "GSE143758"  
    pmid = "28602351"
    download_dir = f"/fs/ess/PAS1475/Weidong/ssKIND/scRNA/raw/PMID{pmid}/"
    if not target_gse_id or not target_gse_id.startswith("GSE"):
        print("Please provide a valid GSE ID (e.g., 'GSE280731').")
    else:
        download_gse_supplementary_files(target_gse_id,download_dir)
