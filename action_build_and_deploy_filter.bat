z:
cd oomlout_oomp_current_version_messy
python action_build_oomp.py -f warehouse
git add *
git commit -m "Build and deploy"
git push