import setuptools


setuptools.setup(
    name             = 'automl-efficientdet',
    version          = '0.0.0',
    description      = '',
    url              = 'https://github.com/google/automl',
    author           = 'Google',
    author_email     = '',
    maintainer       = '',
    maintainer_email = '',
    packages         = setuptools.find_packages(),
    install_requires = [
        'lxml>=4.6.1',
        'absl-py>=0.10.0',
        'matplotlib>=3.0.3',
        'numpy>=1.19.4',
        'Pillow>=6.0.0',
        'PyYAML>=5.1',
        'six>=1.15.0',
        'tensorflow>=2.4.0',
        'tensorflow-addons>=0.12',
        'tensorflow-hub>=0.11',
        'neural-structured-learning>=1.3.1',
        'tensorflow-model-optimization>=0.5',
        'Cython>=0.29.13'
    ],
    entry_points     = {
        'console_scripts': [
            'efficientdet-tf-model-inspect=efficientdet.model_inspect:launcher',
            'efficientdet-tf-main=efficientdet.main:launcher',
            'efficientdet-keras-train=efficientdet.keras.train:launcher',
            'efficientdet-keras-inspector=efficientdet.keras.inspector:launcher',
            'efficientdet-keras-eval=efficientdet.keras.eval:launcher',
            'efficientdet-create-coco-tfrecord=efficientdet.dataset.create_coco_tfrecord:launcher',
            'efficientdet-create-pascal-tfrecord=efficientdet.dataset.create_pascal_tfrecord:launcher',
            'efficientdet-inspect-tfrecord=efficientdet.dataset.inspect_tfrecords:launcher'
        ],
    }
)
