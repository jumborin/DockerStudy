FROM sameersbn/redmine:4.2.0
#FROM sameersbn/redmine:latest

COPY scm.yml /home/redmine/redmine/config
COPY default /etc/nginx/sites-available

RUN set -ux \
    && apt update \
#    && apy upgrade -y \
#    && apt install -y -no-install-recommends update-manager \
#    && apt dist-upgrade \
#    && do-release-upgrade \
    && apt-get install -y --no-install-recommends gosu \
    && rm -rf /var/lib/apt/lists/* \
    
    && gosu redmine git config --global http.sslverify false \
    && gosu redmine git clone --depth 1 https://github.com/akiko-pusu/redmine_banner.git plugins/redmine_banner \
    && gosu redmine git clone --depth 1 https://github.com/redmica/redmine_issues_panel.git plugins/redmine_issues_panel \
    && gosu redmine git clone --depth 1 https://github.com/AlphaNodes/redmine_messenger.git plugins/redmine_messenger \
    && gosu redmine git clone --depth 1 https://github.com/farend/scm-creator.git plugins/redmine_scm \
    && gosu redmine git clone --depth 1 https://github.com/haru/redmine_wiki_extensions.git plugins/redmine_wiki_extensions \
    && gosu redmine git clone --depth 1 https://github.com/gtt-project/sidebar_hide.git plugins/sidebar_hide \
    && gosu redmine git clone --depth 1 https://github.com/onozaty/redmine-view-customize.git plugins/view_customize \
    
    && gosu redmine git clone -b redmine4.1 --depth 1 https://github.com/farend/redmine_theme_farend_bleuclair.git public/themes/bleuclair \
    && gosu redmine git clone --depth 1 https://github.com/farend/redmine_theme_farend_basic.git public/themes/farend_basic \
    && gosu redmine git clone --depth 1 https://github.com/ChrisMcKee/redmine-themes.git public/themes/CM-Red \
    && gosu redmine git clone --depth 1 https://github.com/makotokw/redmine-theme-gitmike.git public/themes/gitmike \
    
    && gosu redmine bundle install --no-cache \
    
    && mkdir -p /home/redmine/data/repos/svn \
    && chown www-data:www-data /home/redmine/data/repos/svn \
    && chmod 0755 /home/redmine/data/repos/svn 
    
