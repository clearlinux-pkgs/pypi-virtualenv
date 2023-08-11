#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-virtualenv
Version  : 20.24.3
Release  : 195
URL      : https://files.pythonhosted.org/packages/77/f9/f6319b17869e66571966060051894d7a6dc77feceb25a9ebb6daee7eed5a/virtualenv-20.24.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/77/f9/f6319b17869e66571966060051894d7a6dc77feceb25a9ebb6daee7eed5a/virtualenv-20.24.3.tar.gz
Summary  : Virtual Python Environment builder
Group    : Development/Tools
License  : MIT
Requires: pypi-virtualenv-bin = %{version}-%{release}
Requires: pypi-virtualenv-license = %{version}-%{release}
Requires: pypi-virtualenv-python = %{version}-%{release}
Requires: pypi-virtualenv-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# virtualenv
[![PyPI](https://img.shields.io/pypi/v/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
[![Documentation](https://readthedocs.org/projects/virtualenv/badge/?version=latest&style=flat-square)](http://virtualenv.pypa.io)
[![Discord](https://img.shields.io/discord/803025117553754132)](https://discord.gg/pypa)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/virtualenv?style=flat-square)](https://pypistats.org/packages/virtualenv)
[![PyPI - License](https://img.shields.io/pypi/l/virtualenv?style=flat-square)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/pypa/virtualenv/workflows/check/badge.svg?branch=main&event=push)](https://github.com/pypa/virtualenv/actions?query=workflow%3Acheck)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

%package bin
Summary: bin components for the pypi-virtualenv package.
Group: Binaries
Requires: pypi-virtualenv-license = %{version}-%{release}

%description bin
bin components for the pypi-virtualenv package.


%package license
Summary: license components for the pypi-virtualenv package.
Group: Default

%description license
license components for the pypi-virtualenv package.


%package python
Summary: python components for the pypi-virtualenv package.
Group: Default
Requires: pypi-virtualenv-python3 = %{version}-%{release}

%description python
python components for the pypi-virtualenv package.


%package python3
Summary: python3 components for the pypi-virtualenv package.
Group: Default
Requires: python3-core
Provides: pypi(virtualenv)
Requires: pypi(distlib)
Requires: pypi(filelock)
Requires: pypi(platformdirs)

%description python3
python3 components for the pypi-virtualenv package.


%prep
%setup -q -n virtualenv-20.24.3
cd %{_builddir}/virtualenv-20.24.3
pushd ..
cp -a virtualenv-20.24.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691777487
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-virtualenv
cp %{_builddir}/virtualenv-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-virtualenv/bcaf1877d014a17d06f0e23264c6429acf921d01 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/virtualenv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-virtualenv/bcaf1877d014a17d06f0e23264c6429acf921d01

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
