Name:           oossh
Version:        0.1.0
Release:        1%{?dist}
Summary:        Capability-bounded SSH client with hardware security key authentication.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oossh
Source0:        oossh-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oossh is a sovereign, capability-bounded SECURE SHELL written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oossh
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oossh-uninstall

%files
/usr/bin/oossh
/usr/bin/oossh-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
