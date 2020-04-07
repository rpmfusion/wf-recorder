# -*-Mode: rpm-spec-mode; -*-

Name:     wf-recorder
Version:  0.2
Release:  3%{?dist}
Summary:  Screen recorder for wlroots-based compositors eg swaywm
License:  MIT
URL:      https://github.com/ammen99/wf-recorder
Source0:  %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%ifarch ppc64le
# fix compilation on ppc64le (gcc#58241)
%global configure_flags -Dcpp_std=gnu++11
%endif

BuildRequires: gcc-c++
BuildRequires: ffmpeg-devel
BuildRequires: meson
BuildRequires: ocl-icd-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: scdoc
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

%description
wf-recorder is a utility program for screen recording of wlroots-based
compositors (more specifically, those that support wlr-screencopy-v1
and xdg-output). Its dependencies are ffmpeg, wayland-client and
wayland-protocols.

%prep
%autosetup

%build
%meson %{?configure_flags}
%meson_build

%install
%meson_install

%files
%{_bindir}/wf-recorder*

%doc README.md
%{_mandir}/man1/%{name}.1.*

%license LICENSE

%changelog
* Mon Apr 06 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2-3
- fixed release tag

* Wed Feb 25 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2-2
- fix ppc64le compile error ref. https://bugzilla.rpmfusion.org/show_bug.cgi?id=5527

* Tue Feb 18 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2-1
- fix release string

* Wed Feb 12 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2-1
- Initial version of the package
