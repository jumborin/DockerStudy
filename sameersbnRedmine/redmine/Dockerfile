FROM sameersbn/redmine:5.0.0

RUN set -ux \
    && apt update \
#    && apt upgrade -y \
#    && apt install -y -no-install-recommends update-manager \
#    && apt dist-upgrade \
#    && do-release-upgrade \
    && apt-get install -y --no-install-recommends gosu \
    && rm -rf /var/lib/apt/lists/* \
    
    && gosu redmine git config --global http.sslverify false \
    && gosu redmine git clone --depth 1 https://github.com/akiko-pusu/redmine_banner.git plugins/redmine_banner \
    && gosu redmine git clone --depth 1 https://github.com/redmica/redmine_issues_panel.git plugins/redmine_issues_panel \
    #&& gosu redmine git clone --depth 1 https://github.com/AlphaNodes/redmine_messenger.git plugins/redmine_messenger \
    #&& gosu redmine git clone --depth 1 https://github.com/farend/scm-creator.git plugins/redmine_scm \
    && gosu redmine git clone --depth 1 https://github.com/haru/redmine_wiki_extensions.git plugins/redmine_wiki_extensions \
    #&& gosu redmine git clone --depth 1 https://github.com/gtt-project/sidebar_hide.git plugins/sidebar_hide \
    && gosu redmine git clone --depth 1 https://github.com/onozaty/redmine-view-customize.git plugins/view_customize \
    #&& gosu redmine git clone --depth 1 https://github.com/haru/redmine_logs.git plugins/redmine_logs \
    
    
    #&& gosu redmine git clone --depth 1  https://github.com/suer/redmine_issues_summary_graph.git plugins/redmine_issues_summary \
    #&& gosu redmine git clone --depth 1  https://github.com/suer/redmine_japanese_help.git plugins/redmine_japanese_help \
    #&& gosu redmine git clone --depth 1  https://github.com/suer/redmine_export_with_journals.git plugins/redmine_export_with_journals \
    #&& gosu redmine git clone --depth 1  https://github.com/suer/redmine_glanceyear.git plugins/redmine_glanceyear \
    #&& gosu redmine git clone --depth 1  https://github.com/suer/redmine_paste_as_markdown_tables.git plugins/redmine_paste_as_markdown_tables \
    #&& gosu redmine git clone --depth 1  https://github.com/peclik/clipboard_image_paste.git plugins/clipboard_image_paste \
    #&& gosu redmine git clone --depth 1  https://github.com/ergoserv/redmine-progressive-projects-list.git plugins/redmine-progressive-projects-list \
    
    && gosu redmine git clone -b redmine4.1 --depth 1 https://github.com/farend/redmine_theme_farend_bleuclair.git public/themes/bleuclair \
    && gosu redmine git clone --depth 1 https://github.com/farend/redmine_theme_farend_basic.git public/themes/farend_basic \
    && gosu redmine git clone --depth 1 https://github.com/ChrisMcKee/redmine-themes.git public/themes/CM-Red \
    && gosu redmine git clone --depth 1 https://github.com/makotokw/redmine-theme-gitmike.git public/themes/gitmike \

    && gosu redmine bundle install --no-cache
    