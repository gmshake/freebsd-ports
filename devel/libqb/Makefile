# Created by: David Shane Holden <dpejesh@yahoo.com>

PORTNAME=		libqb
DISTVERSIONPREFIX=	v
DISTVERSION=		2.0.4
CATEGORIES=		devel

MAINTAINER=		egypcio@FreeBSD.org
COMMENT=		High performance logging, tracing, ipc, and polling library

LICENSE=		LGPL21
LICENSE_FILE=		${WRKSRC}/COPYING

LIB_DEPENDS=		libxml2.so:textproc/libxml2
TEST_DEPENDS=		checkmk:devel/check

GROUPS=			haclient

QB_SOCKET_DIR?=		/var/run/qb
PLIST_SUB+=		QB_SOCKET_DIR=${QB_SOCKET_DIR}

USES=			autoreconf cpe gmake libtool pathfix pkgconfig python
CPE_VENDOR=		clusterlabs
USE_BINUTILS=		yes
USE_GITHUB=		yes
USE_LDCONFIG=		yes

GH_ACCOUNT=		ClusterLabs

GNU_CONFIGURE=		yes
CONFIGURE_ARGS=		--with-socket-dir=${QB_SOCKET_DIR} \
			PACKAGE_STRING="${PORTNAME} ${PORTVERSION}" \
			PACKAGE_VERSION=${PORTVERSION}
LDFLAGS+=		-B${LOCALBASE}/bin
PATHFIX_MAKEFILEIN=	Makefile.am

INSTALL_TARGET=		install-strip
TEST_TARGET=		check

OPTIONS_DEFINE=		DOCS DOXYGEN
OPTIONS_SUB=		yes

DOXYGEN_IMPLIES=	DOCS
DOXYGEN_BUILD_DEPENDS=	doxygen:devel/doxygen

post-patch:
	${REINPLACE_CMD} -e 's/doxygen2man//g' ${WRKSRC}/Makefile.am

post-install:
	${MKDIR} ${STAGEDIR}${QB_SOCKET_DIR}

.include <bsd.port.mk>
