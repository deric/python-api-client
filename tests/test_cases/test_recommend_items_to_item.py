#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.item_to_item_recommendation import ItemToItemRecommendationTest
from recombee_api_client.api_requests import *

class RecommendItemsToItemTestCase (ItemToItemRecommendationTest):

    def create_request(self, item_id, target_user_id, count, user_impact=None, filter=None, booster=None, cascade_create=None, scenario=None, return_properties=None, included_properties=None, diversity=None, min_relevance=None, rotation_rate=None, rotation_time=None, expert_settings=None):
        return RecommendItemsToItem(item_id, target_user_id, count, user_impact=user_impact, filter=filter, booster=booster, cascade_create=cascade_create, scenario=scenario, return_properties=return_properties, included_properties=included_properties, diversity=diversity, min_relevance=min_relevance, rotation_rate=rotation_rate, rotation_time=rotation_time, expert_settings=expert_settings)
