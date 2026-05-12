from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in salon_management/__init__.py
from salon import __version__ as version

setup(
	name="salon",
	version=version,
	description="Salon and spa post-booking customer management application",
	author="Your Company Name",
	author_email="contact@yourcompany.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
