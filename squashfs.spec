Summary:	Set of tools which creates squashfs filesystem
Name:		squashfs
Version:	4.3
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://downloads.sourceforge.net/squashfs/%{name}%{version}.tar.gz
# Source0-md5:	d92ab59aabf5173f2a59089531e30dbf
URL:		http://squashfs.sourceforge.net/
BuildRequires:	lz4-devel
BuildRequires:	lzo-devel
BuildRequires:	sed
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains utilities for squashfs filesystem.

Squashfs is a highly compressed read-only filesystem for Linux (kernel
2.4.x and 2.6.x). It uses zlib compression to compress both files,
inodes and directories. Inodes in the system are very small and all
blocks are packed to minimise data overhead. Block sizes greater than
4K are supported up to a maximum of 64K.

Squashfs is intended for general read-only filesystem use, for
archival use (i.e. in cases where a .tar.gz file may be used), and in
constrained block device/memory systems (e.g. embedded systems) where
low overhead is needed.

%prep
%setup -qn %{name}%{version}

%{__sed} -i 's|-O2 |%{rpmcflags}|g' squashfs-tools/Makefile

%build
%{__make} -C squashfs-tools	\
	CC="%{__cc}"		\
	LZ4_SUPPORT=1		\
	LZO_SUPPORT=1		\
	XZ_SUPPORT=1

%install
rm -rf $RPM_BUILD_ROOT

install -D squashfs-tools/mksquashfs $RPM_BUILD_ROOT%{_sbindir}/mksquashfs
install squashfs-tools/unsquashfs $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc *README*
%attr(755,root,root) %{_sbindir}/*

