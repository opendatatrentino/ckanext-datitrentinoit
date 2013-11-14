# Makefile to build CSS and JS resources

# Requires:
#  - a Ckan working copu
#  - cssmin and uglify-js: npm -g install uglify-js cssmin

CKAN_DIR := $(HOME)/Projects/dati-trentino-2/ckan
CSSMIN := cssmin
UGLIFY := uglify
LESSC := lessc


MAIN_CSS := static/css/main.css
MAIN_CSS_FILES = \
    $(CKAN_DIR)/ckan/public/css/boilerplate.css \
    $(CKAN_DIR)/ckan/public/css/chosen.css \
    $(CKAN_DIR)/ckan/public/css/handheld.css \
    $(CKAN_DIR)/ckan/public/css/bootstrap.min.css \
    $(CKAN_DIR)/ckan/public/css/style.css \
    $(CKAN_DIR)/ckan/public/css/forms.css \
    $(CKAN_DIR)/ckan/public/base/css/main.css

VENDOR_CSS := static/css/vendor.css
VENDOR_CSS_FILES = \
    $(CKAN_DIR)/ckan/public/base/vendor/bootstrap/less/tests/css-tests.css \
    $(CKAN_DIR)/ckan/public/base/vendor/select2/select2.css \
    $(CKAN_DIR)/ckan/public/base/vendor/font-awesome/css/font-awesome.css \
    $(CKAN_DIR)/ckan/public/scripts/dataexplorer/table-view.css \
    $(CKAN_DIR)/ckan/public/scripts/vendor/jqueryui/1.8.14/css/jquery-ui.custom.css \
    $(CKAN_DIR)/ckan/public/scripts/vendor/jquery.fileupload/20110801/jquery.fileupload-ui.css \
    $(CKAN_DIR)/ckan/public/scripts/vendor/leaflet/0.3.1/leaflet.css \
    $(CKAN_DIR)/ckan/public/scripts/vendor/recline/css/recline.css \
    $(CKAN_DIR)/ckan/public/scripts/vendor/openid-selector/css/openid.css \
    $(CKAN_DIR)/ckan/public/scripts/vendor/slickgrid/2.0.1/slick.grid.css

VENDOR_CSS_IE := static/css/vendor-ie.css
VENDOR_CSS_IE_FILES = \
    $(CKAN_DIR)/ckan/public/base/vendor/font-awesome/css/font-awesome-ie7.css \
    $(CKAN_DIR)/ckan/public/scripts/vendor/leaflet/0.3.1/leaflet.ie.css

PLUGIN_CUSTOM_CSS := static/css/datitrentino.css
PLUGIN_CUSTOM_CSS_FILES = \
    ../fanstatic/styles/less/datitrentinoit.less

FONTAWESOME_FONTS := \
    static/font/FontAwesome.otf \
    static/font/fontawesome-webfont.ttf \
    static/font/fontawesome-webfont.eot \
    static/font/fontawesome-webfont.svg \
    static/font/fontawesome-webfont.woff
FONTAWESOME_FONT_SRC = $(CKAN_DIR)/ckan/public/base/vendor/font-awesome/font/%
FONTAWESOME_FONT_DST = static/font/%


FOOTER_JS := static/js/footer-scripts.js
VENDOR_JS_DIR = $(CKAN_DIR)/ckan/public/base/vendor
BASE_JS_DIR = $(CKAN_DIR)/ckan/public/base/javascript
FOOTER_JS_FILES = \
    $(VENDOR_JS_DIR)/jquery.min.js \
    $(VENDOR_JS_DIR)/bootstrap/js/bootstrap.min.js \
    $(VENDOR_JS_DIR)/jed.min.js \
    $(VENDOR_JS_DIR)/select2/select2.min.js \
    $(BASE_JS_DIR)/plugins/jquery.inherit.js \
    $(BASE_JS_DIR)/plugins/jquery.proxy-all.js \
    $(BASE_JS_DIR)/plugins/jquery.url-helpers.js \
    $(BASE_JS_DIR)/plugins/jquery.date-helpers.js \
    $(BASE_JS_DIR)/plugins/jquery.slug.js \
    $(BASE_JS_DIR)/plugins/jquery.slug-preview.js \
    $(BASE_JS_DIR)/plugins/jquery.truncator.js \
    $(BASE_JS_DIR)/plugins/jquery.masonry.js \
    $(BASE_JS_DIR)/plugins/jquery.form-warning.js \
    $(BASE_JS_DIR)/sandbox.js \
    $(BASE_JS_DIR)/module.js \
    $(BASE_JS_DIR)/pubsub.js \
    $(BASE_JS_DIR)/client.js \
    $(BASE_JS_DIR)/notify.js \
    $(BASE_JS_DIR)/i18n.js \
    $(BASE_JS_DIR)/main.js \
    $(BASE_JS_DIR)/modules/select-switch.js \
    $(BASE_JS_DIR)/modules/slug-preview.js \
    $(BASE_JS_DIR)/modules/basic-form.js \
    $(BASE_JS_DIR)/modules/confirm-action.js \
    $(BASE_JS_DIR)/modules/api-info.js \
    $(BASE_JS_DIR)/modules/autocomplete.js \
    $(BASE_JS_DIR)/modules/custom-fields.js \
    $(BASE_JS_DIR)/modules/related-item.js \
    $(BASE_JS_DIR)/modules/data-viewer.js \
    $(BASE_JS_DIR)/modules/table-selectable-rows.js \
    $(BASE_JS_DIR)/modules/resource-form.js \
    $(BASE_JS_DIR)/modules/resource-upload-field.js \
    $(BASE_JS_DIR)/modules/follow.js \
    $(BASE_JS_DIR)/modules/activity-stream.js \
    $(BASE_JS_DIR)/modules/dashboard.js \
    $(BASE_JS_DIR)/modules/table-toggle-more.js \
    $(BASE_JS_DIR)/modules/dataset-visibility.js \
    $(BASE_JS_DIR)/modules/media-grid.js

ALL_CSS_TARGETS = $(MAIN_CSS) $(VENDOR_CSS) $(VENDOR_CSS_IE) $(PLUGIN_CUSTOM_CSS)
ALL_JS_TARGETS = $(FOOTER_JS)


all: all_css all_js all_fonts

clean: clean_css clean_js clean_fonts


all_css: $(ALL_CSS_TARGETS)

clean_css:
	rm -f $(ALL_CSS_TARGETS)

all_js: $(ALL_JS_TARGETS)

clean_js:
	rm -f $(ALL_JS_TARGETS)

all_fonts: $(FONTAWESOME_FONTS)

clean_fonts:
	rm -f $(FONTAWESOME_FONTS)


$(MAIN_CSS): $(MAIN_CSS_FILES)
	mkdir -p $(dir $@)
	cat $^ | $(CSSMIN) > $@

$(VENDOR_CSS): $(VENDOR_CSS_FILES)
	mkdir -p $(dir $@)
	cat $^ | $(CSSMIN) > $@

$(VENDOR_CSS_IE): $(VENDOR_CSS_IE_FILES)
	mkdir -p $(dir $@)
	cat $^ | $(CSSMIN) > $@

$(PLUGIN_CUSTOM_CSS): $(PLUGIN_CUSTOM_CSS_FILES)
	mkdir -p $(dir $@)
	$(LESSC) $^ > $@

$(FOOTER_JS): $(FOOTER_JS_FILES)
	mkdir -p $(dir $@)
	$(UGLIFY) $^ -c -o $@

$(FONTAWESOME_FONTS): $(FONTAWESOME_FONT_DST): $(FONTAWESOME_FONT_SRC)
	mkdir -p $(dir $@)
	cp $< $@
