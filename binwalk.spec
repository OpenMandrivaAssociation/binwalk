Name:		binwalk
Version:	0.4.2
Release:	1
Summary:	A tool for identifying files embedded inside firmware images
Group:		System/Configuration/Other 
License:	MIT
URL:		http://code.google.com/p/binwalk/
Source0:	http://binwalk.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:	zlib1-devel
BuildRequires:	curl-devel

%description
Binwalk is a tool for searching a given binary 
image for embedded files and executable code.
Specifically, it is designed for identifying files
and code embedded inside of firmware images.
Binwalk uses the libmagic library, so it is
compatible with magic signatures
created for the Unix file utility.

Binwalk also includes a custom magic signature file
which contains improved signatures for files that are
commonly found in firmware images such
as compressed/archived files, firmware headers,
Linux kernels, bootloaders, filesystems, etc. 

%prep
%setup -q


%build
cd src/
%configure2_5x
%make

%install
cd src/
%makeinstall_std

%files
%{_bindir}/%{name}
%{_sysconfdir}/%{name}/magic.binarch
%{_sysconfdir}/%{name}/magic.bincast
%{_sysconfdir}/%{name}/magic.binwalk
%{_sysconfdir}/%{name}/magic.o


%changelog
* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.2-1
+ Revision: 778034
- rpmlint desc fix
- version update 0.4.2

* Wed Dec 07 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.4.1-1
+ Revision: 738535
- imported package binwalk

