LESSC := lessc

CSS_OUTPUT := datitrentinoit.css
LESS_MAIN := less/datitrentinoit.less
LESS_ALL := $(wildcard less/*.less) $(wildcard less/contrib/*.less)

all: $(CSS_OUTPUT)

$(CSS_OUTPUT): $(LESS_MAIN) $(LESS_ALL)
	$(LESSC) $< > $@

clean:
	rm -f $(CSS_OUTPUT)
