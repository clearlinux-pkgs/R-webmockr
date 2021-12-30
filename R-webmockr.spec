#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-webmockr
Version  : 0.8.0
Release  : 39
URL      : https://cran.r-project.org/src/contrib/webmockr_0.8.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/webmockr_0.8.0.tar.gz
Summary  : Stubbing and Setting Expectations on 'HTTP' Requests
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-base64enc
Requires: R-crul
Requires: R-curl
Requires: R-fauxpas
Requires: R-jsonlite
Requires: R-magrittr
Requires: R-urltools
BuildRequires : R-R6
BuildRequires : R-base64enc
BuildRequires : R-crul
BuildRequires : R-curl
BuildRequires : R-fauxpas
BuildRequires : R-jsonlite
BuildRequires : R-magrittr
BuildRequires : R-urltools
BuildRequires : buildreq-R

%description
Includes tools for stubbing 'HTTP' requests, including expected
    request conditions and response conditions. Match on
    'HTTP' method, query parameters, request body, headers and
    more. Can be used for unit tests or outside of a testing 
    context.

%prep
%setup -q -c -n webmockr
cd %{_builddir}/webmockr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615822352

%install
export SOURCE_DATE_EPOCH=1615822352
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
/usr/lib64/R/library/webmockr/tests/testthat/crul_body_upload_list.rda
/usr/lib64/R/library/webmockr/tests/testthat/crul_body_upload_no_list.rda
/usr/lib64/R/library/webmockr/tests/testthat/crul_obj.rda
/usr/lib64/R/library/webmockr/tests/testthat/helper-webmockr.R
/usr/lib64/R/library/webmockr/tests/testthat/httr_body_upload_list.rda
/usr/lib64/R/library/webmockr/tests/testthat/httr_body_upload_no_list.rda
/usr/lib64/R/library/webmockr/tests/testthat/httr_obj.rda
/usr/lib64/R/library/webmockr/tests/testthat/httr_obj_auth.rda
/usr/lib64/R/library/webmockr/tests/testthat/test-Adapter.R
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
/usr/lib64/R/library/webmockr/tests/testthat/test-auth_handling.R
/usr/lib64/R/library/webmockr/tests/testthat/test-b-no-cassette-in-use.R
/usr/lib64/R/library/webmockr/tests/testthat/test-flipswitch.R
/usr/lib64/R/library/webmockr/tests/testthat/test-onload.R
/usr/lib64/R/library/webmockr/tests/testthat/test-pluck_body.R
/usr/lib64/R/library/webmockr/tests/testthat/test-remove_request_stub.R
/usr/lib64/R/library/webmockr/tests/testthat/test-request_registry.R
/usr/lib64/R/library/webmockr/tests/testthat/test-stub_registry.R
/usr/lib64/R/library/webmockr/tests/testthat/test-stub_request.R
/usr/lib64/R/library/webmockr/tests/testthat/test-stub_requests_crul.R
/usr/lib64/R/library/webmockr/tests/testthat/test-to_raise.R
/usr/lib64/R/library/webmockr/tests/testthat/test-to_return.R
/usr/lib64/R/library/webmockr/tests/testthat/test-to_return_body.R
/usr/lib64/R/library/webmockr/tests/testthat/test-to_return_then.R
/usr/lib64/R/library/webmockr/tests/testthat/test-to_timeout.R
/usr/lib64/R/library/webmockr/tests/testthat/test-uri_regex.R
/usr/lib64/R/library/webmockr/tests/testthat/test-webmockr_reset.R
/usr/lib64/R/library/webmockr/tests/testthat/test-wi_th.R
/usr/lib64/R/library/webmockr/tests/testthat/test-within_test_that_blocks.R
/usr/lib64/R/library/webmockr/tests/testthat/test-writing-to-disk-write_disk_path.R
/usr/lib64/R/library/webmockr/tests/testthat/test-writing-to-disk.R
/usr/lib64/R/library/webmockr/tests/testthat/test-zutils.R
