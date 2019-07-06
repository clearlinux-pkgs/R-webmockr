#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-webmockr
Version  : 0.3.4
Release  : 17
URL      : https://cran.r-project.org/src/contrib/webmockr_0.3.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/webmockr_0.3.4.tar.gz
Summary  : Stubbing and Setting Expectations on 'HTTP' Requests
Group    : Development/Tools
License  : MIT
BuildRequires : R-crul
BuildRequires : R-curl
BuildRequires : R-fauxpas
BuildRequires : R-jsonlite
BuildRequires : R-lazyeval
BuildRequires : R-urltools
BuildRequires : buildreq-R

%description
webmockr
========
[![cran checks](https://cranchecks.info/badges/worst/webmockr)](https://cranchecks.info/pkgs/webmockr)
[![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Build Status](https://travis-ci.org/ropensci/webmockr.svg?branch=master)](https://travis-ci.org/ropensci/webmockr)
[![Build status](https://ci.appveyor.com/api/projects/status/47scc0vur41sbfyx?svg=true)](https://ci.appveyor.com/project/sckott/webmockr)
[![codecov](https://codecov.io/gh/ropensci/webmockr/branch/master/graph/badge.svg)](https://codecov.io/gh/ropensci/webmockr)
[![rstudio mirror downloads](http://cranlogs.r-pkg.org/badges/webmockr)](https://github.com/metacran/cranlogs.app)
[![cran version](https://www.r-pkg.org/badges/version/webmockr)](https://cran.r-project.org/package=webmockr)

%prep
%setup -q -c -n webmockr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552919483

%install
export SOURCE_DATE_EPOCH=1552919483
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library webmockr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library webmockr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library webmockr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/webmockr/DESCRIPTION
/usr/lib64/R/library/webmockr/INDEX
/usr/lib64/R/library/webmockr/LICENSE
/usr/lib64/R/library/webmockr/Meta/Rd.rds
/usr/lib64/R/library/webmockr/Meta/features.rds
/usr/lib64/R/library/webmockr/Meta/hsearch.rds
/usr/lib64/R/library/webmockr/Meta/links.rds
/usr/lib64/R/library/webmockr/Meta/nsInfo.rds
/usr/lib64/R/library/webmockr/Meta/package.rds
/usr/lib64/R/library/webmockr/NAMESPACE
/usr/lib64/R/library/webmockr/NEWS.md
/usr/lib64/R/library/webmockr/R/webmockr
/usr/lib64/R/library/webmockr/R/webmockr.rdb
/usr/lib64/R/library/webmockr/R/webmockr.rdx
/usr/lib64/R/library/webmockr/help/AnIndex
/usr/lib64/R/library/webmockr/help/aliases.rds
/usr/lib64/R/library/webmockr/help/paths.rds
/usr/lib64/R/library/webmockr/help/webmockr.rdb
/usr/lib64/R/library/webmockr/help/webmockr.rdx
/usr/lib64/R/library/webmockr/html/00Index.html
/usr/lib64/R/library/webmockr/html/R.css
/usr/lib64/R/library/webmockr/ignore/adapter-httr.R
/usr/lib64/R/library/webmockr/ignore/sockets.R
/usr/lib64/R/library/webmockr/tests/test-all.R
/usr/lib64/R/library/webmockr/tests/testthat/crul_obj.rda
/usr/lib64/R/library/webmockr/tests/testthat/helper-webmockr.R
/usr/lib64/R/library/webmockr/tests/testthat/httr_obj.rda
/usr/lib64/R/library/webmockr/tests/testthat/test-CrulAdapter.R
/usr/lib64/R/library/webmockr/tests/testthat/test-HashCounter.R
/usr/lib64/R/library/webmockr/tests/testthat/test-HttpLibAdapaterRegistry.R
/usr/lib64/R/library/webmockr/tests/testthat/test-HttrAdapter.R
/usr/lib64/R/library/webmockr/tests/testthat/test-RequestPattern.R
/usr/lib64/R/library/webmockr/tests/testthat/test-RequestRegistry.R
/usr/lib64/R/library/webmockr/tests/testthat/test-RequestSignature.R
/usr/lib64/R/library/webmockr/tests/testthat/test-Response.R
/usr/lib64/R/library/webmockr/tests/testthat/test-StubRegistry.R
/usr/lib64/R/library/webmockr/tests/testthat/test-StubbedRequest.R
/usr/lib64/R/library/webmockr/tests/testthat/test-b-no-cassette-in-use.R
/usr/lib64/R/library/webmockr/tests/testthat/test-flipswitch.R
/usr/lib64/R/library/webmockr/tests/testthat/test-onload.R
/usr/lib64/R/library/webmockr/tests/testthat/test-remove_request_stub.R
/usr/lib64/R/library/webmockr/tests/testthat/test-request_registry.R
/usr/lib64/R/library/webmockr/tests/testthat/test-stub_request.R
/usr/lib64/R/library/webmockr/tests/testthat/test-stub_requests_crul.R
/usr/lib64/R/library/webmockr/tests/testthat/test-to_raise.R
/usr/lib64/R/library/webmockr/tests/testthat/test-to_return.R
/usr/lib64/R/library/webmockr/tests/testthat/test-to_return_body.R
/usr/lib64/R/library/webmockr/tests/testthat/test-to_timeout.R
/usr/lib64/R/library/webmockr/tests/testthat/test-wi_th.R
/usr/lib64/R/library/webmockr/tests/testthat/test-within_test_that_blocks.R
/usr/lib64/R/library/webmockr/tests/testthat/test-zutils.R
