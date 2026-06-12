# Implementation Tasks

## Overview

This document outlines the implementation tasks for the Website Image Replacement system. Tasks are organized by component and include both implementation and testing responsibilities.

---

## Phase 1: Core Infrastructure and Data Models

### Task 1.1: Setup Project Structure and Dependencies

**Description**: Initialize the project with TypeScript configuration, install required dependencies, and setup the basic directory structure.

**Acceptance Criteria**:
- [-] Initialize npm project with TypeScript 5.0+
- [~] Install core dependencies: sharp, image-size, jsdom, fs-extra, glob
- [~] Install testing dependencies: vitest, fast-check, @testing-library/dom
- [~] Create src/ directory structure: components/, models/, utils/, types/
- [~] Configure TypeScript with strict mode and proper module resolution
- [~] Setup vitest configuration for unit and property-based testing

**Estimated Effort**: 2 hours

**Dependencies**: None

---

### Task 1.2: Implement Core Data Models

**Description**: Create TypeScript interfaces and types for ImageMetadata, ImageInventory, ImageMapping, and ReplacementConfig.

**Acceptance Criteria**:
- [~] Create ImageMetadata interface with all required fields (path, filename, width, height, aspectRatio, fileSize, format, usageContext, category, lastModified)
- [~] Create ImageCategory enum with all category values
- [~] Create ImageInventory interface with images array, categorized map, totalCount, and byFormat
- [~] Create ImageMapping interface with mappings, confidence, alternatives, unmapped, and metadata
- [~] Create ReplacementConfig interface with all configuration options
- [~] Add validation helper functions for each data model
- [~] Write unit tests for validation functions

**Estimated Effort**: 4 hours

**Dependencies**: Task 1.1

---

## Phase 2: ImageAnalyzer Component

### Task 2.1: Implement Image File Discovery

**Description**: Implement directory scanning to discover all image files with supported extensions.

**Acceptance Criteria**:
- [~] Implement scanDirectory() function to recursively find image files
- [~] Support extensions: jpg, jpeg, png, svg, gif, webp
- [~] Handle directory traversal errors gracefully
- [~] Return array of file paths
- [~] Write unit tests for various directory structures
- [~] Write property test: For any directory, all files with valid extensions are discovered (Property 1)

**Estimated Effort**: 4 hours

**Dependencies**: Task 1.2

---

### Task 2.2: Implement Image Metadata Extraction

**Description**: Extract metadata from image files including dimensions, file size, and format.

**Acceptance Criteria**:
- [~] Implement analyzeImage() function using sharp library
- [~] Extract width, height, file size, format
- [~] Calculate aspect ratio as width / height
- [~] Get file modification timestamp
- [~] Handle corrupted/invalid images gracefully with warnings
- [~] Write unit tests for different image formats
- [~] Write property test: For any valid image, all metadata fields are populated (Property 2)
- [~] Write property test: For any image with positive dimensions, aspectRatio = width / height (Property 4)

**Estimated Effort**: 5 hours

**Dependencies**: Task 2.1

---

### Task 2.3: Implement Image Categorization

**Description**: Categorize images based on file path, name patterns, and usage context.

**Acceptance Criteria**:
- [~] Implement categorizeByUsage() function
- [~] Detect categories from path patterns (e.g., /logo/, /banner/, /course/)
- [~] Detect categories from filename patterns
- [~] Assign default category "general" when no pattern matches
- [~] Ensure each image gets exactly one category
- [~] Write unit tests for different path/name patterns
- [~] Write property test: For any image, exactly one valid category is assigned (Property 3)

**Estimated Effort**: 3 hours

**Dependencies**: Task 2.2

---

### Task 2.4: Build Complete Image Inventory

**Description**: Combine discovery, metadata extraction, and categorization into complete inventory generation.

**Acceptance Criteria**:
- [~] Implement buildInventory() function that orchestrates all scanning steps
- [~] Create categorized map grouping images by category
- [~] Create byFormat map grouping images by format
- [~] Set totalCount to match images array length
- [~] Write unit tests with sample image directories
- [~] Write property test: Inventory structure contains all required fields (Property 5)

**Estimated Effort**: 3 hours

**Dependencies**: Task 2.3

---

## Phase 3: MappingEngine Component

### Task 3.1: Implement Match Score Calculator

**Description**: Implement the algorithm to calculate match scores between old and new images.

**Acceptance Criteria**:
- [~] Implement calculateMatchScore() function
- [~] Apply weights: category (40%), aspect ratio (30%), dimension (20%), format (10%)
- [~] Ensure score is always between 0 and 1
- [~] Handle edge cases (missing metadata, zero dimensions)
- [~] Write unit tests with known input/output pairs
- [~] Write property test: All scores are in range [0, 1] (Property 7)
- [~] Write property test: Scoring weights are correctly applied (Property 8)

**Estimated Effort**: 4 hours

**Dependencies**: Task 1.2

---

### Task 3.2: Implement Core Mapping Algorithm

**Description**: Create the main algorithm that maps existing images to new images.

**Acceptance Criteria**:
- [~] Implement createMapping() function
- [~] Sort existing images by priority (logo first, banner, etc.)
- [~] For each existing image, find best match from unused new images
- [~] Track used new images to prevent duplicate assignments
- [~] Populate mappings, confidence, alternatives, and unmapped lists
- [~] Write unit tests with various inventory combinations
- [~] Write property test: Every existing image is mapped or unmapped (Property 6)
- [~] Write property test: No new image is used more than once (Property 12)

**Estimated Effort**: 6 hours

**Dependencies**: Task 3.1

---

### Task 3.3: Implement Mapping Quality Checks

**Description**: Add logic to flag mappings that need review based on confidence and aspect ratio.

**Acceptance Criteria**:
- [~] Flag mappings with confidence < 0.5 as low-confidence
- [~] Flag mappings with aspect ratio difference > 0.2 as requiring review
- [~] Add flags to mapping metadata
- [~] Write unit tests for flagging logic
- [~] Write property test: Aspect ratio mismatches are flagged (Property 9)
- [~] Write property test: Low confidence mappings are marked (Property 10)

**Estimated Effort**: 3 hours

**Dependencies**: Task 3.2

---

### Task 3.4: Implement Alternative Suggestions

**Description**: Provide alternative mapping suggestions for low-confidence mappings.

**Acceptance Criteria**:
- [~] Track top 3 alternative candidates during scoring
- [~] Store alternatives in mapping object
- [~] Ensure alternatives are different from primary mapping
- [~] Write unit tests verifying alternatives
- [~] Write property test: Low-confidence mappings with 3+ candidates have 3+ alternatives (Property 11)

**Estimated Effort**: 3 hours

**Dependencies**: Task 3.2

---

### Task 3.5: Implement Mapping Export and Import

**Description**: Add functionality to export mappings to JSON and import them back.

**Acceptance Criteria**:
- [~] Implement exportMapping() to create JSON configuration file
- [~] Include all mappings, confidence scores, alternatives, and metadata in export
- [~] Implement importMapping() to parse JSON configuration
- [~] Validate imported mapping structure and referenced paths
- [~] Support manual modifications to exported mappings
- [~] Write unit tests for export/import
- [~] Write property test: Exported mapping is valid JSON (Property 48)
- [~] Write property test: Export includes all required data (Property 49)
- [~] Write property test: Import validates structure and paths (Property 50)
- [~] Write property test: Export then import preserves mapping (Property 51)

**Estimated Effort**: 4 hours

**Dependencies**: Task 3.2

---

## Phase 4: HTMLUpdater Component

### Task 4.1: Implement HTML Parsing

**Description**: Parse HTML files into DOM structure for manipulation.

**Acceptance Criteria**:
- [~] Implement parseHTMLFile() using jsdom
- [~] Handle malformed HTML gracefully
- [~] Preserve original HTML structure
- [~] Return parsed DOM document
- [~] Write unit tests with various HTML structures
- [~] Handle large HTML files efficiently

**Estimated Effort**: 3 hours

**Dependencies**: Task 1.1

---

### Task 4.2: Implement Image Reference Discovery

**Description**: Find all image references in HTML including img tags and CSS background-image.

**Acceptance Criteria**:
- [~] Implement findImageReferences() function
- [~] Discover all img elements with src attributes
- [~] Discover background-image in inline style attributes
- [~] Discover background-image in style elements
- [~] Record metadata: element type, attribute, path, line number, context
- [~] Normalize all paths for consistent comparison
- [~] Write unit tests for different reference types
- [~] Write property test: All img elements are discovered (Property 17)
- [~] Write property test: Inline background-images are discovered (Property 18)
- [~] Write property test: Style element background-images are discovered (Property 19)
- [~] Write property test: Reference metadata is complete (Property 20)
- [~] Write property test: Path normalization is consistent (Property 21)

**Estimated Effort**: 5 hours

**Dependencies**: Task 4.1

---

### Task 4.3: Implement Image Reference Updates

**Description**: Update image references in HTML based on mapping.

**Acceptance Criteria**:
- [~] Implement updateImageReferences() function
- [~] Update img src attributes with new paths
- [~] Update background-image URLs in styles while preserving other CSS properties
- [~] Skip references without mappings and log them
- [~] Track update statistics (updated, skipped, errors)
- [~] Write unit tests for different update scenarios
- [~] Write property test: All mappable references are updated (Property 22)
- [~] Write property test: Unmapped references are preserved (Property 23)
- [~] Write property test: CSS properties are preserved during background updates (Property 24)

**Estimated Effort**: 5 hours

**Dependencies**: Task 4.2

---

### Task 4.4: Implement HTML Validation

**Description**: Validate HTML structure before and after updates.

**Acceptance Criteria**:
- [~] Implement validateHTML() using html-validate
- [~] Check for structural validity
- [~] Check for broken references
- [~] Return detailed validation results
- [~] Write unit tests with valid and invalid HTML
- [~] Write property test: Valid HTML remains valid after updates (Property 26)

**Estimated Effort**: 3 hours

**Dependencies**: Task 4.1

---

### Task 4.5: Implement HTML File Saving

**Description**: Save updated HTML back to files while preserving formatting.

**Acceptance Criteria**:
- [~] Implement saveHTMLFile() function
- [~] Preserve HTML structure and element hierarchy
- [~] Preserve non-image attributes
- [~] Preserve formatting where possible
- [~] Handle file write errors gracefully
- [~] Write unit tests for save operations
- [~] Write property test: Non-image attributes are preserved (Property 27)

**Estimated Effort**: 2 hours

**Dependencies**: Task 4.4

---

### Task 4.6: Implement Batch Update Operations

**Description**: Process multiple HTML files in batch with parallel processing.

**Acceptance Criteria**:
- [~] Implement batchUpdateFiles() function
- [~] Process files in parallel for performance
- [~] Continue processing on individual file errors
- [~] Aggregate statistics from all files
- [~] Generate detailed batch report
- [~] Write unit tests with multiple files
- [~] Write property test: Batch statistics are accurate (Property 25)
- [~] Write property test: Parallel updates maintain consistency (Property 46)
- [~] Write property test: Error resilience in batch processing (Property 32)

**Estimated Effort**: 5 hours

**Dependencies**: Task 4.5

---

### Task 4.7: Implement Idempotent Update Logic

**Description**: Ensure applying the same mapping multiple times produces consistent results.

**Acceptance Criteria**:
- [~] Detect when references already match target mapping
- [~] Skip redundant updates
- [~] Ensure update(update(html)) = update(html)
- [~] Write unit tests for idempotence
- [~] Write property test: Double application equals single application (Property 40)
- [~] Write property test: Pre-updated references result in zero updates (Property 41)

**Estimated Effort**: 3 hours

**Dependencies**: Task 4.3

---

## Phase 5: TestPreviewGenerator Component

### Task 5.1: Implement Preview HTML Structure Generator

**Description**: Generate the base HTML structure for the preview page.

**Acceptance Criteria**:
- [~] Create HTML template with sections for each category
- [~] Include CSS for side-by-side comparison layout
- [~] Include JavaScript for interactive features (toggle, zoom)
- [~] Make preview standalone (no external dependencies)
- [~] Write unit tests for structure generation

**Estimated Effort**: 4 hours

**Dependencies**: Task 1.2

---

### Task 5.2: Implement Comparison View Generator

**Description**: Create side-by-side comparison views for individual image mappings.

**Acceptance Criteria**:
- [~] Implement createComparisonView() function
- [~] Display old and new images side by side
- [~] Show dimensions, aspect ratios, and confidence scores
- [~] Highlight low-confidence mappings with warning indicators
- [~] Include category labels
- [~] Write unit tests for comparison generation
- [~] Write property test: One comparison per mapping (Property 13)
- [~] Write property test: Comparisons contain all required information (Property 14)
- [~] Write property test: Low confidence mappings show warnings (Property 15)

**Estimated Effort**: 4 hours

**Dependencies**: Task 5.1

---

### Task 5.3: Implement Category-Based Organization

**Description**: Organize comparisons by image category in the preview.

**Acceptance Criteria**:
- [~] Group comparisons by category
- [~] Add category headers
- [~] Sort categories in meaningful order
- [~] Write unit tests for organization logic
- [~] Write property test: Comparisons are organized by category (Property 16)

**Estimated Effort**: 2 hours

**Dependencies**: Task 5.2

---

### Task 5.4: Implement Preview Generation and Export

**Description**: Combine all preview components and save to HTML file.

**Acceptance Criteria**:
- [~] Implement generatePreview() function
- [~] Combine structure, comparisons, and organization
- [~] Include inline CSS and JavaScript
- [~] Implement savePreview() to write file
- [~] Write unit tests for complete preview generation
- [~] Validate generated HTML is well-formed

**Estimated Effort**: 3 hours

**Dependencies**: Task 5.3

---

## Phase 6: System Integration and Orchestration

### Task 6.1: Implement Configuration Validation

**Description**: Validate ReplacementConfig before processing begins.

**Acceptance Criteria**:
- [~] Implement validateConfig() function
- [~] Validate projectRoot is absolute path and exists
- [~] Validate image directories are accessible
- [~] Validate htmlFiles array contains at least one valid HTML file
- [~] Validate backup path is writable if backup enabled
- [~] Return descriptive error messages for failures
- [~] Write unit tests for various invalid configs
- [~] Write property test: Project root validation (Property 35)
- [~] Write property test: Image directories validation (Property 36)
- [~] Write property test: HTML files validation (Property 37)
- [~] Write property test: Backup path validation (Property 38)
- [~] Write property test: Validation error messages are descriptive (Property 39)

**Estimated Effort**: 4 hours

**Dependencies**: Task 1.2

---

### Task 6.2: Implement Path Security Validation

**Description**: Prevent directory traversal and ensure all paths are within project root.

**Acceptance Criteria**:
- [~] Implement path validation functions
- [~] Reject paths with ".." directory traversal sequences
- [~] Normalize paths to canonical form before validation
- [~] Verify all resolved paths are within project root
- [~] Log security warnings for rejected paths
- [~] Write unit tests with malicious paths
- [~] Write property test: Directory traversal is rejected (Property 42)
- [~] Write property test: Paths are contained within root (Property 43)
- [~] Write property test: Out-of-root paths are rejected with warning (Property 44)
- [~] Write property test: Normalization occurs before validation (Property 45)

**Estimated Effort**: 3 hours

**Dependencies**: Task 6.1

---

### Task 6.3: Implement Backup System

**Description**: Create backup of files before modification.

**Acceptance Criteria**:
- [~] Implement createBackup() function
- [~] Copy all HTML files and image directories to backup location
- [~] Include timestamp in backup directory name
- [~] Halt processing if backup fails when enabled
- [~] Skip backup if disabled (with confirmation)
- [~] Write unit tests for backup creation
- [~] Write property test: Backup created before modification when enabled (Property 28)
- [~] Write property test: Backup contains all required files (Property 29)
- [~] Write property test: Backup has correct location and timestamp (Property 30)

**Estimated Effort**: 4 hours

**Dependencies**: Task 6.1

---

### Task 6.4: Implement Error Handling and Reporting

**Description**: Add comprehensive error handling and reporting throughout the system.

**Acceptance Criteria**:
- [~] Implement error logging with detailed context
- [~] Continue processing after non-critical errors
- [~] Generate detailed completion report
- [~] Report specific errors for permission issues
- [~] Exit early without modifications on critical errors
- [~] Write unit tests for error scenarios
- [~] Write property test: Error logging is complete (Property 31)
- [~] Write property test: Critical errors preserve file system (Property 34)
- [~] Write property test: Completion reports are complete (Property 33)

**Estimated Effort**: 4 hours

**Dependencies**: Task 6.1

---

### Task 6.5: Implement Main Orchestration Function

**Description**: Create the main processImageReplacement() function that orchestrates all components.

**Acceptance Criteria**:
- [~] Implement processImageReplacement() function
- [~] Validate configuration first
- [~] Create backup if enabled
- [~] Scan existing and new images
- [~] Create mapping
- [~] Generate preview
- [~] Wait for user approval (if not dry run)
- [~] Update HTML files
- [~] Generate final report
- [~] Write integration tests for complete workflow

**Estimated Effort**: 5 hours

**Dependencies**: Tasks 2.4, 3.2, 4.6, 5.4, 6.4

---

## Phase 7: Performance Optimization

### Task 7.1: Implement Image Metadata Caching

**Description**: Cache image metadata to avoid re-scanning unchanged images.

**Acceptance Criteria**:
- [~] Implement cache storage in .cache/image-metadata.json
- [~] Check file modification timestamps to invalidate stale cache entries
- [~] Use cached metadata for unchanged images
- [~] Write cache to disk after scan
- [~] Write unit tests for cache operations
- [~] Write property test: Cached unchanged images are not re-scanned (Property 47)

**Estimated Effort**: 4 hours

**Dependencies**: Task 2.4

---

### Task 7.2: Implement Parallel Image Processing

**Description**: Process images concurrently using worker threads.

**Acceptance Criteria**:
- [~] Use worker threads for parallel metadata extraction
- [~] Limit concurrent workers to 4-8 based on CPU cores
- [~] Handle worker errors gracefully
- [~] Aggregate results from all workers
- [~] Write unit tests for parallel processing
- [~] Measure performance improvement

**Estimated Effort**: 5 hours

**Dependencies**: Task 2.2

---

### Task 7.3: Optimize HTML Parsing and Updates

**Description**: Improve performance of HTML operations for large projects.

**Acceptance Criteria**:
- [~] Use streaming for large HTML files
- [~] Cache parsed DOM structures for frequently accessed files
- [~] Optimize image reference search algorithms
- [~] Write performance benchmarks
- [~] Verify 30-second target for 50 files

**Estimated Effort**: 4 hours

**Dependencies**: Task 4.6

---

## Phase 8: CLI and User Interface

### Task 8.1: Implement Command-Line Interface

**Description**: Create CLI for running the image replacement system.

**Acceptance Criteria**:
- [~] Implement CLI using commander or yargs
- [~] Support command-line arguments for all config options
- [~] Support loading config from JSON file
- [~] Display progress indicators during processing
- [~] Display final report in readable format
- [~] Write integration tests for CLI

**Estimated Effort**: 5 hours

**Dependencies**: Task 6.5

---

### Task 8.2: Implement Dry Run Mode

**Description**: Add dry run mode that generates preview without making changes.

**Acceptance Criteria**:
- [~] Add --dry-run flag to CLI
- [~] Skip HTML updates in dry run mode
- [~] Generate preview and report only
- [~] Display what would be changed
- [~] Write integration tests for dry run

**Estimated Effort**: 2 hours

**Dependencies**: Task 8.1

---

### Task 8.3: Implement Interactive Approval

**Description**: Add interactive approval step before applying changes.

**Acceptance Criteria**:
- [~] Display preview statistics
- [~] Prompt user for confirmation
- [~] Allow user to review preview before confirming
- [~] Handle cancellation gracefully
- [~] Skip approval in automated mode

**Estimated Effort**: 3 hours

**Dependencies**: Task 8.1

---

## Phase 9: Testing and Documentation

### Task 9.1: Write Integration Tests

**Description**: Create comprehensive integration tests for the complete system.

**Acceptance Criteria**:
- [~] Test complete workflow from scan to update
- [~] Test with sample project containing multiple HTML files
- [~] Test error recovery scenarios
- [~] Test backup and restore functionality
- [~] Test with various image types and formats
- [~] Verify performance benchmarks are met

**Estimated Effort**: 6 hours

**Dependencies**: Task 8.1

---

### Task 9.2: Enhance Property-Based Tests

**Description**: Expand property-based test coverage for all correctness properties.

**Acceptance Criteria**:
- [~] Ensure all 51 correctness properties have corresponding property tests
- [~] Configure fast-check generators for ImageMetadata, ImageMapping, HTML documents
- [~] Set minimum 100 iterations per property test
- [~] Tag tests with feature name and property number
- [~] Verify all tests pass with randomized inputs

**Estimated Effort**: 8 hours

**Dependencies**: All component implementation tasks

---

### Task 9.3: Write User Documentation

**Description**: Create comprehensive user documentation.

**Acceptance Criteria**:
- [~] Write README with installation instructions
- [~] Document all CLI commands and options
- [~] Provide usage examples for common scenarios
- [~] Document configuration file format
- [~] Create troubleshooting guide
- [~] Document backup and recovery procedures

**Estimated Effort**: 4 hours

**Dependencies**: Task 8.1

---

### Task 9.4: Write Developer Documentation

**Description**: Create documentation for developers contributing to the project.

**Acceptance Criteria**:
- [~] Document architecture and component interactions
- [~] Document data models and interfaces
- [~] Document testing approach and conventions
- [~] Create contribution guidelines
- [~] Document build and development workflow

**Estimated Effort**: 3 hours

**Dependencies**: Task 9.3

---

## Phase 10: Deployment and Validation

### Task 10.1: Test on Real Purdue Website

**Description**: Run the system on the actual Purdue website project to validate functionality.

**Acceptance Criteria**:
- [~] Create backup of current Purdue website
- [~] Run system in dry-run mode first
- [~] Review generated preview thoroughly
- [~] Manually verify sample image replacements
- [~] Check responsive behavior on multiple screen sizes
- [~] Validate all HTML pages after replacement
- [~] Test in multiple browsers (Chrome, Firefox, Safari)

**Estimated Effort**: 4 hours

**Dependencies**: Task 9.1

---

### Task 10.2: Performance Validation

**Description**: Validate that performance requirements are met on the real project.

**Acceptance Criteria**:
- [~] Measure image scanning time for Purdue project
- [~] Measure mapping creation time
- [~] Measure preview generation time
- [~] Measure HTML batch update time
- [~] Measure total workflow time
- [~] Verify all times are within specified targets
- [~] Document performance results

**Estimated Effort**: 2 hours

**Dependencies**: Task 10.1

---

### Task 10.3: Create Release Package

**Description**: Package the system for distribution and deployment.

**Acceptance Criteria**:
- [~] Build production version with optimizations
- [~] Create npm package configuration
- [~] Include all necessary dependencies
- [~] Test installation from package
- [~] Create release notes
- [~] Tag release version in git

**Estimated Effort**: 3 hours

**Dependencies**: Tasks 9.3, 9.4, 10.2

---

## Task Summary

**Total Estimated Effort**: ~130 hours (approximately 3-4 weeks for one developer)

**Critical Path**:
1. Phase 1: Infrastructure (6 hours)
2. Phase 2: ImageAnalyzer (15 hours)
3. Phase 3: MappingEngine (20 hours)
4. Phase 4: HTMLUpdater (26 hours)
5. Phase 5: TestPreviewGenerator (13 hours)
6. Phase 6: Integration (20 hours)
7. Phase 7: Optimization (13 hours)
8. Phase 8: CLI (10 hours)
9. Phase 9: Testing & Docs (21 hours)
10. Phase 10: Deployment (9 hours)

**Priority Order**:
- **High Priority**: Phases 1-6 (core functionality)
- **Medium Priority**: Phases 7-8 (performance and usability)
- **Low Priority**: Phases 9-10 (documentation and deployment)

**Parallelization Opportunities**:
- ImageAnalyzer, MappingEngine, and TestPreviewGenerator can be developed in parallel after Phase 1
- HTMLUpdater can start after Phase 1
- Testing can be done incrementally alongside development

---

## Notes

- All property-based tests should use fast-check with minimum 100 iterations
- All property tests should be tagged with: `Feature: website-image-replacement, Property {N}: {property_text}`
- Integration tests should use realistic sample data from the Purdue website
- Performance benchmarks should be automated and run in CI/CD pipeline
- Security validation (path traversal prevention) should be thoroughly tested with malicious inputs
