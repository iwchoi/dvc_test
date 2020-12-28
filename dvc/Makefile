#/*--
# DVC test   
#
# Written by Ickwon Choi, Net-Targets
# iwchoi@net-targets.com 
#
# Copyright (c) 2020, Net-Targets
# All rights reserved.
#--*/

all:
	@dvc repro 

pull: 
	@cd .. && dvc pull

dag:
	@dvc dag --dot | dot -Tpng > pipelines.png
