import logging
import shutil
from . import tools
from . import common
from pathlib import Path

def clean(args, board):
  logging.info(f"Cleaning {board.name} in {board.build_dir}")
  
  shutil.rmtree(board.build_dir)


def prepare(args, board):
  t = tools.tools(args)
  logging.info(f"Preparing {board.name} in {board.build_dir}")

  l4t_path = Path(board.build_dir) / "Linux_for_Tegra"

  if l4t_path.exists():
    logging.info(f"L4T path {l4t_path} exists, not extracting")
  else:
    logging.info("Extracting driver package")
    t.extract(board.files.driver_package, board.build_dir, sudo=True)

  rootfs_path = l4t_path / "rootfs"

  # Arbitrary choice of a directory which exists in the rootfs tarball
  if (rootfs_path / "lib").exists():
    logging.info(f"Rootfs {rootfs_path} exists, not extracting")
  else:
    logging.info("Extracting rootfs")
    t.extract(board.files.rootfs, str(rootfs_path), sudo=True)

  logging.warning("Extracting public_sources DISABLED")
  #t.extract(board.files.public_sources, board.build_dir)
  #t.execute(['sudo', './apply_binaries.sh'], cwd=board.build_dir / 'Linux_for_Tegra')
  
