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

  if (Path(board.build_dir) / "Linux_for_Tegra").exists():
    logging.info(f"Driver package exists, not extracting")
  else:
    logging.info("Extracting driver package")
    t.extract(board.files.driver_package, board.build_dir, sudo=True)

  # Need to choose a file which exists in rootfs
  if not (Path(board.build_dir) / "Linux_for_Tegra" / "rootfs" / "etc" / "hosts" ).exists():
    logging.info("Extracting rootfs")
    t.extract(board.files.rootfs, board.build_dir / 'Linux_for_Tegra/rootfs', sudo=True)


  logging.warning("Extracting public_sources DISABLED")
  #t.extract(board.files.public_sources, board.build_dir)
  #t.execute(['sudo', './apply_binaries.sh'], cwd=board.build_dir / 'Linux_for_Tegra')
  
