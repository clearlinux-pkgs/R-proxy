#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-proxy
Version  : 0.4.26
Release  : 41
URL      : https://cran.r-project.org/src/contrib/proxy_0.4-26.tar.gz
Source0  : https://cran.r-project.org/src/contrib/proxy_0.4-26.tar.gz
Summary  : Distance and Similarity Measures
Group    : Development/Tools
License  : GPL-2.0
Requires: R-proxy-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-proxy package.
Group: Libraries

%description lib
lib components for the R-proxy package.


%prep
%setup -q -c -n proxy
cd %{_builddir}/proxy

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623164419

%install
export SOURCE_DATE_EPOCH=1623164419
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library proxy
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library proxy
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library proxy
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc proxy || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/proxy/DESCRIPTION
/usr/lib64/R/library/proxy/INDEX
/usr/lib64/R/library/proxy/Meta/Rd.rds
/usr/lib64/R/library/proxy/Meta/features.rds
/usr/lib64/R/library/proxy/Meta/hsearch.rds
/usr/lib64/R/library/proxy/Meta/links.rds
/usr/lib64/R/library/proxy/Meta/nsInfo.rds
/usr/lib64/R/library/proxy/Meta/package.rds
/usr/lib64/R/library/proxy/Meta/vignette.rds
/usr/lib64/R/library/proxy/NAMESPACE
/usr/lib64/R/library/proxy/NEWS.Rd
/usr/lib64/R/library/proxy/R/proxy
/usr/lib64/R/library/proxy/R/proxy.rdb
/usr/lib64/R/library/proxy/R/proxy.rdx
/usr/lib64/R/library/proxy/doc/index.html
/usr/lib64/R/library/proxy/doc/overview.R
/usr/lib64/R/library/proxy/doc/overview.Rnw
/usr/lib64/R/library/proxy/doc/overview.pdf
/usr/lib64/R/library/proxy/help/AnIndex
/usr/lib64/R/library/proxy/help/aliases.rds
/usr/lib64/R/library/proxy/help/paths.rds
/usr/lib64/R/library/proxy/help/proxy.rdb
/usr/lib64/R/library/proxy/help/proxy.rdx
/usr/lib64/R/library/proxy/html/00Index.html
/usr/lib64/R/library/proxy/html/R.css
/usr/lib64/R/library/proxy/tests/apply.R
/usr/lib64/R/library/proxy/tests/apply.Rout.save
/usr/lib64/R/library/proxy/tests/distance.R
/usr/lib64/R/library/proxy/tests/distance.Rout.save
/usr/lib64/R/library/proxy/tests/distcalls.R
/usr/lib64/R/library/proxy/tests/distcalls.Rout.save
/usr/lib64/R/library/proxy/tests/registry.R
/usr/lib64/R/library/proxy/tests/registry.Rout.save
/usr/lib64/R/library/proxy/tests/util.R
/usr/lib64/R/library/proxy/tests/util.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/proxy/libs/proxy.so
/usr/lib64/R/library/proxy/libs/proxy.so.avx2
