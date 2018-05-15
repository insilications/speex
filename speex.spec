#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : speex
Version  : 1.2rc2
Release  : 13
URL      : https://ftp.osuosl.org/pub/xiph/releases/speex/speex-1.2rc2.tar.gz
Source0  : https://ftp.osuosl.org/pub/xiph/releases/speex/speex-1.2rc2.tar.gz
Summary  : An open-source, patent-free speech codec
Group    : Development/Tools
License  : BSD-3-Clause
Requires: speex-bin
Requires: speex-lib
Requires: speex-doc
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(ogg)
BuildRequires : pkgconfig(speexdsp)
BuildRequires : speexdsp-dev

%description
Speex is a patent-free audio codec designed especially for voice (unlike 
Vorbis which targets general audio) signals and providing good narrowband 
and wideband quality. This project aims to be complementary to the Vorbis
codec.

%package bin
Summary: bin components for the speex package.
Group: Binaries

%description bin
bin components for the speex package.


%package dev
Summary: dev components for the speex package.
Group: Development
Requires: speex-lib
Requires: speex-bin
Provides: speex-devel

%description dev
dev components for the speex package.


%package doc
Summary: doc components for the speex package.
Group: Documentation

%description doc
doc components for the speex package.


%package lib
Summary: lib components for the speex package.
Group: Libraries

%description lib
lib components for the speex package.


%prep
%setup -q -n speex-1.2rc2
pushd ..
cp -a speex-1.2rc2 buildavx2
popd
pushd ..
cp -a speex-1.2rc2 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526426976
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffast-math -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffast-math -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffast-math -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffast-math -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-vectorize "
%configure --disable-static --enable-sse
make  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --enable-sse   --libdir=/usr/lib64/haswell --bindir=/usr/bin/haswell
make  %{?_smp_mflags}
popd
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=skylake-avx512"
export CXXFLAGS="$CXXFLAGS -m64 -march=skylake-avx512"
export LDFLAGS="$LDFLAGS -m64 -march=skylake-avx512"
%configure --disable-static --enable-sse   --libdir=/usr/lib64/haswell/avx512_1 --bindir=/usr/bin/haswell/avx512_1
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526426976
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install
popd
pushd ../buildavx512/
%make_install
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haswell/avx512_1/speexdec
/usr/bin/haswell/avx512_1/speexenc
/usr/bin/haswell/speexdec
/usr/bin/haswell/speexenc
/usr/bin/speexdec
/usr/bin/speexenc

%files dev
%defattr(-,root,root,-)
/usr/include/speex/speex.h
/usr/include/speex/speex_bits.h
/usr/include/speex/speex_callbacks.h
/usr/include/speex/speex_config_types.h
/usr/include/speex/speex_header.h
/usr/include/speex/speex_stereo.h
/usr/include/speex/speex_types.h
/usr/lib64/haswell/libspeex.so
/usr/lib64/libspeex.so
/usr/lib64/pkgconfig/speex.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/speex/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libspeex.so
/usr/lib64/haswell/avx512_1/libspeex.so.1
/usr/lib64/haswell/avx512_1/libspeex.so.1.5.0
/usr/lib64/haswell/libspeex.so.1
/usr/lib64/haswell/libspeex.so.1.5.0
/usr/lib64/libspeex.so.1
/usr/lib64/libspeex.so.1.5.0
