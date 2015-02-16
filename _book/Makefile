# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
BUILDDIR      = _book
RESDIR        = resource



doc: build page commit
	@echo
	@echo "==========================================================="
	@echo "    VisualOps Documents has been Generated Successful!!!"
	@echo "==========================================================="
	@echo


build: 
	-git checkout master
	gitbook build


page:
	-git branch -D gh-pages
	#git checkout --orphan gh-pages
	git symbolic-ref HEAD refs/heads/gh-pages

	ls -1|grep -v "^$(BUILDDIR)$$"|xargs rm -rf
	mv $(BUILDDIR)/* .
	
	rm -r $(BUILDDIR)
	@echo
	@echo "==========================================================="
	@echo "    GitHub Pages has been Generated Successful!!!"
	@echo "==========================================================="
	@echo

co_master:
	-git checkout master


commit:
	-git add -A
	-git commit -a --no-edit -m "Robot: Auto Deploy"


deploy:
	git push origin gh-pages:gh-pages -f

	@echo
	@echo "==========================================================="
	@echo "    GitHub Pages has been Deployed!!!"
	@echo "==========================================================="
	@echo


help:
	@echo "make                  to build and gernerate gh-pages branch"
	@echo "make deploy           to deploy to github"


clean:
	rm -rf $(BUILDDIR)



