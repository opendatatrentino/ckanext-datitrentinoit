LESSC := lessc
CSSMIN := cssmin

CSS_OUTPUT := datitrentinoit.css
CSS_MIN_OUTPUT := datitrentinoit.min.css
LESS_MAIN := less/datitrentinoit.less
LESS_ALL := $(wildcard less/*.less) $(wildcard less/contrib/*.less)
ALL_TARGETS := $(CSS_OUTPUT) $(CSS_MIN_OUTPUT)


all: $(ALL_TARGETS)

$(CSS_OUTPUT): $(LESS_MAIN) $(LESS_ALL)
	$(LESSC) $< > $@

$(CSS_MIN_OUTPUT): $(CSS_OUTPUT)
	$(CSSMIN) < $< > $@

clean:
	rm -f $(ALL_TARGETS)
