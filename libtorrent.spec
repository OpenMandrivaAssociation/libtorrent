%define major 46
%define oldlibname %mklibname torrent 40
%define libname %mklibname torrent
%define libnamedev %mklibname -d torrent

#define _disable_lto 1

Name:		libtorrent
Version:	0.16.16
Release:	1
Summary:	BitTorrent library written in C++ for *nix
License:	GPLv2+
Group:		Networking/File transfer
URL:		https://github.com/rakshasa/libtorrent
#Source0:	https://rtorrent.net/downloads/%{name}-%{version}.tar.gz
Source0:   https://github.com/rakshasa/rtorrent/releases/download/v%{version}/libtorrent-%{version}.tar.gz

BuildSystem:	autotools
BuildOption:	--enable-ipv6
BuildOption:	--with-posix-fallocate
BuildRequires:  make
BuildRequires:	autoconf
BuildRequires:	slibtool
BuildRequires:	atomic-devel
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires: 	pkgconfig(openssl)
#gw only if autoconf/automake is called:
BuildRequires:	automake
BuildRequires:	cppunit-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(zlib)

%description
LibTorrent is a BitTorrent library written in C++ for *nix. It is designed to
avoid redundant copying and storing of data that other clients and libraries
suffer from. Licensed under the GPL.

Basic features have been implemented and a ncurses client is included. Sloppy
and biased test runs have shown that transferring a 200 MB file with libTorrent
uses 1/4 of the CPU time that the official BitTorrent client requires.

The library and client are under heavy development. They are stable enough to
handle any torrents I throw at them these days. 

%package -n %{libname}
Summary:	BitTorrent library written in C++ for *nix
Group:		System/Libraries
Provides:	%{name} = %{EVRD}
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %libname
LibTorrent is a BitTorrent library written in C++ for *nix. It is designed to
avoid redundant copying and storing of data that other clients and libraries
suffer from. Licensed under the GPL.

Basic features have been implemented and a ncurses client is included. Sloppy
and biased test runs have shown that transferring a 200 MB file with libTorrent
uses 1/4 of the CPU time that the official BitTorrent client requires.

The library and client are under heavy development. They are stable enough to
handle any torrents I throw at them these days. 

%package -n %{libnamedev}
Summary:	BitTorrent library written in C++ for *nix
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%mklibname -d %name 10

%description -n %libnamedev
LibTorrent is a BitTorrent library written in C++ for *nix. It is designed to
avoid redundant copying and storing of data that other clients and libraries
suffer from. Licensed under the GPL.

Basic features have been implemented and a ncurses client is included. Sloppy
and biased test runs have shown that transferring a 200 MB file with libTorrent
uses 1/4 of the CPU time that the official BitTorrent client requires.

The library and client are under heavy development. They are stable enough to
handle any torrents I throw at them these days. 

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{libnamedev}
%{_libdir}/lib*.so
%{_includedir}/torrent/
%{_libdir}/pkgconfig/%{name}.pc
