# Generated by rust2rpm 21
%bcond_without check
%global debug_package %{nil}

%global crate integer-encoding

Name:           rust-%{crate}
Version:        3.0.3
Release:        %autorelease
Summary:        Varint+zigzag and fixedint integer encoding/decoding (https://developers.google.com/protocol-buffers/docs/encoding)

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/integer-encoding
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Varint+zigzag and fixedint integer encoding/decoding
(https://developers.google.com/protocol-buffers/docs/encoding).}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-trait-devel %{_description}

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%files       -n %{name}+async-trait-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-util-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%files       -n %{name}+futures-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures_async-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures_async-devel %{_description}

This package contains library source intended for building other packages which
use the "futures_async" feature of the "%{crate}" crate.

%files       -n %{name}+futures_async-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio_async-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio_async-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio_async" feature of the "%{crate}" crate.

%files       -n %{name}+tokio_async-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
