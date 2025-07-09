%define _empty_manifest_terminate_build 0

Name:          binwalk
Version:       3.1.0
Release:       1
Summary:       Firmware Analysis Tool
License:       MIT
URL:           https://github.com/ReFirmLabs/binwalk
Source0:       https://github.com/ReFirmLabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: rust
BuildRequires: cargo

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
%autosetup

%build
cargo build --release --locked

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 "target/release/%{name}" %{buildroot}%{_bindir}

%check
# https://github.com/ReFirmLabs/binwalk/issues/882
# cargo test --release --locked

%files
%license LICENSE
%{_bindir}/%{name}
