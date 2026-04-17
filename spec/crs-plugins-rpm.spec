Summary: Plugins for CoreRuleSet
Name: mod_security_crs_plugins
Version: 1.0
Release: 0%{?dist}
License: ASL 2.0
URL: https://github.com/german-gonzalez-ruiz/mod_security_crs_plugins
Group: System Environment/Daemons

Source0: https://codeload.github.com/german-gonzalez-ruiz/mod_security_crs_plugins/tar.gz/refs/tags/v%{version}
Source1: https://raw.githubusercontent.com/german-gonzalez-ruiz/crs-plugins-rpm/main/config/plugin-default-config.conf
Source2: https://raw.githubusercontent.com/german-gonzalez-ruiz/crs-plugins-rpm/main/config/REQUEST-900-0-PLUGINS-CONFIG.conf
Source3: https://raw.githubusercontent.com/german-gonzalez-ruiz/crs-plugins-rpm/main/config/REQUEST-900-EXCLUSION-RULES-PLUGINS-BEFORE-CRS.conf
Source4: https://raw.githubusercontent.com/german-gonzalez-ruiz/crs-plugins-rpm/main/config/RESPONSE-999-EXCLUSION-RULES-PLUGINS-AFTER-CRS.conf

BuildArch: noarch
Requires: mod_security >= 2.9.6
Requires: mod_security_crs >= 4.0.0
Obsoletes: mod_security_crs-extras < 3.0.0

%description
This package provides a minimum set of plugins for OWASP Core Rule set.

%prep
%setup -q -n mod_security_crs_plugins-%{version}

%build

%install
install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/plugins/


# Add Include *-config, *-before and *-after for plugins files
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/plugins/plugin-default-config.conf
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/REQUEST-900-0-PLUGINS-CONFIG.conf
install -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/REQUEST-900-EXCLUSION-RULES-PLUGINS-BEFORE-CRS.conf
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/RESPONSE-999-EXCLUSION-RULES-PLUGINS-AFTER-CRS.conf

# Deploy plugins
mv %{_builddir}/mod_security_crs_plugins-%{version}/* %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/plugins/


%files
%config %{_sysconfdir}/httpd/modsecurity.d/activated_rules/*


%changelog
* Fri Apr 17 2026 German Gonzalez <ggonzalez@tilsor.com.uy> - 1.0
- Installation of plugins for WordPress, Nextcloud, and Drupal for OWASP CRS v4
