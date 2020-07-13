Feature: Video Playback Tests
    Background:
        Given I log into Hudl

    Scenario: Test playback in the VSPA
        When I load the video in the VSPA
        And I pause the video in the VSPA
        And I get the play time in the VSPA
        Then I take a screenshot of the page
        And I set the points in pixels
        And I crop the image
        And I convert the image to text
        And I verify the video played back correctly