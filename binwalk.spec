%define _empty_manifest_terminate_build 0

Name:		binwalk
Version:	3.1.0
Release:	2
Summary:	Firmware Analysis Tool
License:	MIT
URL:		https://github.com/ReFirmLabs/binwalk
Source0:	https://github.com/ReFirmLabs/binwalk/archive/v%{version}/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz

BuildRequires:	cargo
BuildRequires:	help2man
BuildRequires:	rust-packaging
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libzstd)
# Optionals for compression support, plotting, analysis
Recommends:	cabextract
Recommends:	cpio
Recommends:	zutils
Recommends:	mtd-utils
Recommends:	p7zip
# Python modules are for entropy plotting and disassembly support
Recommends:	python%{pyver}dist(capstone)
Recommends:	python%{pyver}dist(lz4)
Recommends:	python%{pyver}dist(matplotlib)
Recommends:	python%{pyver}dist(numpy)
Recommends:	python%{pyver}dist(pyopengl)
Recommends:	python%{pyver}dist(pyqtgraph)
Recommends:	python%{pyver}dist(python-gnupg)
Recommends:	python%{pyver}dist(zstandard)
Recommends:	sleuthkit
Recommends:	squashfs-tools
Recommends:	tar
Recommends:	unrar

%description
Binwalk can identify, and optionally extract, files and
data that have been embedded inside of other files.

While its primary focus is firmware analysis, it supports
a wide variety of file and data types.

Through entropy analysis, it can even help to identify
unknown compression or encryption!

%prep
%autosetup -n %{name}-%{version} -p1 -a1
%cargo_prep -v vendor

cat >>.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CARGO_NET_OFFLINE=true
export CARGO_HOME=$PWD/.cargo
# sort out crate licenses
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%__cargo build --release --locked

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 "target/release/%{name}" %{buildroot}%{_bindir}

help2man %{buildroot}%{_bindir}/binwalk --no-discard-stderr --version-string="%{version}" --no-info > binwalk.1
install -Dpm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
# https://github.com/ReFirmLabs/binwalk/issues/882
# cargo test --release --locked

%files
%doc README.md
%license LICENSE LICENSES.dependencies
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.zst
