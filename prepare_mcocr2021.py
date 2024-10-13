from pathlib import Path
import shutil
import sys
import warnings


if __name__ == '__main__':

    # Path to the "general" data directory
    data_dir = Path(__file__).parent / 'data'

    # Path to the extracted MC-OCR 2021 data directory.
    # If it exists, the extraction process will be terminated
    # and a warning will be issued.
    output_dir = data_dir / 'mcocr2021_public'
    if output_dir.exists():
        warnings.warn('2021 MC-OCR corpus was already prepared.')
        sys.exit(0)

    # Path to the public MC-OCR 2021 data directory (default name)
    public_data_dir = data_dir / 'mcocr_public_train_test_shared_data'
    assert not public_data_dir.is_dir()
    
    # Downloaded compressed data. It needs to be downloaded first.
    compressed_file = data_dir / 'mcocr2021_public_train_test_data.zip'
    assert compressed_file.is_file(), \
        'Please download the compressed data and save to ' \
        '"{}". Read README for more.'.format(compressed_file)
    
    # Extract the data.
    shutil.unpack_archive(compressed_file, data_dir)
    assert public_data_dir.is_dir()
    
    # Rename it to be less verbose.
    public_data_dir.rename(output_dir)

    # Remove __MACOSX directory if it exists.
    deleted_dirs = [data_dir / '__MACOSX']
    for dir_path in deleted_dirs:
        if dir_path.exists():
            shutil.rmtree(dir_path)
