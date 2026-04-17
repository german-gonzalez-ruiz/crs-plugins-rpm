Summary: Plugins for CoreRuleSet
Name: mod_security_crs_plugins
Version: 1.0
Release: 0%{?dist}
License: ASL 2.0
URL: https://github.com/german-gonzalez-ruiz/mod_security_crs_plugins
Group: System Environment/Daemons

Source0: https://codeload.github.com/german-gonzalez-ruiz/mod_security_crs_plugins/tar.gz/refs/tags/v%{version}
Source1: https://raw.githubusercontent.com/german-gonzalez-ruiz/mod_security_crs_plugins/main/config/plugin-default-config.conf
Source2: https://raw.githubusercontent.com/german-gonzalez-ruiz/mod_security_crs_plugins/main/config/REQUEST-900-0-PLUGINS-CONFIG.conf
Source3: https://raw.githubusercontent.com/german-gonzalez-ruiz/mod_security_crs_plugins/main/config/REQUEST-900-EXCLUSION-PLUGINS-BEFORE-CRS.conf
Source4: https://raw.githubusercontent.com/german-gonzalez-ruiz/mod_security_crs_plugins/main/config/RESPONSE-999-EXCLUSION-PLUGINS-AFTER-CRS.conf

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

# Setup plugins default config as disabled
mv config/plugin-default-config.conf %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/plugins/

# To exclude rules (pre/post)
mv config/REQUEST-900-0-PLUGINS-CONFIG.conf %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/REQUEST-900-0-PLUGINS-CONFIG.conf
mv config/REQUEST-900-EXCLUSION-PLUGINS-BEFORE-CRS.conf %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/REQUEST-900-EXCLUSION-PLUGINS-BEFORE-CRS.conf
mv config/RESPONSE-999-EXCLUSION-PLUGINS-AFTER-CRS.conf %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/RESPONSE-999-EXCLUSION-PLUGINS-AFTER-CRS.conf

# Process the set of downloaded plugins to deploy them in an organized manner into their corresponding directory
install -Dp -m0644 %{Source0} %{_tmppath}/plugins/
mv %{_tmppath}/plugins/mod_security_crs_plugins-%{version}/mod_security_crs_plugins-%{version}/* %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/plugins/


%files
%config %{_sysconfdir}/httpd/modsecurity.d/activated_rules/plugins/


%changelog
* Thu Mar 19 2026 German Gonzalez <ggonzalez@tilsor.com.uy> - 1.0
- Installation of plugins for WordPress, Nextcloud, and Drupal for OWASP CRS v4
