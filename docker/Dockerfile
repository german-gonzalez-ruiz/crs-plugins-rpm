FROM rockylinux:8
RUN dnf -y install rpmdevtools rpm-build gcc make && \
    dnf clean all
WORKDIR /root/rpmbuild
# Copiar archivos necesarios (.spec, fuentes)
COPY spec/ /root/rpmbuild/SPECS/
COPY config/ /root/rpmbuild/SOURCES/
# Ejecutar compilación
#CMD ["rpmbuild", "-ba", "SPECS/mod_security_crs.spec"]
CMD spectool -g -R /root/rpmbuild/SPECS/crs-plugins-rpm.spec && \
    rpmbuild -ba /root/rpmbuild/SPECS/crs-plugins-rpm.spec
