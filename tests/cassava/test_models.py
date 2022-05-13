import os

from pytorch_lightning import Trainer

from kaggle_cassava.data import CassavaDataModule
from kaggle_cassava.models import LitCassava, LitMobileNet, LitResnet

from tests import _ROOT_TESTS


def test_create_resnet():
    LitResnet(arch="resnet18")


def test_create_mobnet():
    LitMobileNet(arch="mobilenet_v3_small")


def test_create_model():
    net = LitMobileNet(arch="mobilenet_v3_small")
    LitCassava(model=net)


def test_devel_run(tmpdir, root_path=_ROOT_TESTS):
    """Sample fast dev run..."""
    dm = CassavaDataModule(
        path_csv=os.path.join(root_path, "data_cassava", "train.csv"),
        path_img_dir=os.path.join(root_path, "data_cassava", "train_images"),
        batch_size=1,
        split=0.6,
    )
    net = LitResnet(arch="resnet18")
    model = LitCassava(model=net)

    trainer = Trainer(
        default_root_dir=tmpdir,
        fast_dev_run=True,
        gpus=0,
    )
    dm.setup()
    trainer.fit(model, datamodule=dm)